import logging
import json
import ijson
import os
import shutil
import sys
import traceback
import datetime
import select
from time import sleep
import htcondor
import copy
from glob import glob

from typing import Dict, Any, Tuple, Optional

from .job import job
from .status import FalconryStatus
from . import cli
from .schedd_wrapper import ScheddWrapper

log = logging.getLogger('falconry')


class Counter:
    # just holds few variables used in status print
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.waiting = 0
        self.notSub = 0
        self.idle = 0
        self.run = 0
        self.failed = 0
        self.done = 0
        self.skipped = 0
        self.removed = 0
        self.held = 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Counter):
            return NotImplemented
        return (
            self.waiting == other.waiting
            and self.notSub == other.notSub
            and self.idle == other.idle
            and self.run == other.run
            and self.failed == other.failed
            and self.done == other.done
            and self.skipped == other.skipped
            and self.removed == other.removed
            and self.held == other.held
        )


class manager:
    """Manager holds all jobs and periodically checks their status.

    It also take care of dependent jobs,
    submitting jobs when all dependencies are satisfied.
    These are handled as decorations of the job.

    Arguments:
        mgrDir (str): directory where the manager stores the jobs
        mgrMsg (str): message to be saved in the save file
        maxJobIdle (int): maximum number of idle jobs
        schedd (ScheddWrapper): htcondor schedd wrapper
        keepSaveFiles (int): number of save files to keep, defaults to 2
    """

    reservedNames = ["Message", "Command"]

    def __init__(
        self,
        mgrDir: str,
        mgrMsg: str = "",
        maxJobIdle: int = -1,
        schedd: Optional[ScheddWrapper] = None,
        keepSaveFiles: int = 2,
    ):
        log.info("MONITOR: INIT")

        # Initialize the manager, maily getting the htcondor schedd
        if schedd is not None:
            self.schedd = schedd
        else:
            self.schedd = ScheddWrapper()

        # job collection
        self.jobs: Dict[str, job] = {}
        self.sub_queue: list[job] = []

        # now create a directory where the info about jobs will be save
        if not os.path.exists(mgrDir):
            os.makedirs(mgrDir)
        self.dir = mgrDir
        self.saveFileName = self.dir + "/data.json"
        self.mgrMsg = mgrMsg
        self.command = " ".join(sys.argv)

        self.maxJobIdle = maxJobIdle
        self.curJobIdle = 0
        self.keepSaveFiles = keepSaveFiles

    # check if save file already exists
    def check_savefile_status(self) -> Tuple[bool, Optional[str]]:
        """Checks if the save file already exists. If it does, asks the user
        whether to load existing jobs or start new ones.

        Returns:
            Tuple[bool, Optional[str]]: (True, 'l') if load, (True, 'n') if new,
            (False, None) if error
        """
        if os.path.exists(self.saveFileName):
            log.warning(f"Manager directory {self.dir} already exists!")
            state, var = cli.input_checker(
                {"l": "Load existing jobs", "n": "Start new jobs"}
            )

            # Simplify the output for user interface
            # both unknown/timeout have the same result
            if state == cli.InputState.SUCCESS:
                return True, var
            return False, var
        elif (
            os.path.exists(self.dir)
            and len(glob(f"{self.dir}/{self.saveFileName}.*")) > 0
        ):
            # In principle this could be done manually but this state is
            # so specific (usually running out of space) that it requires
            # additional user intervention anyway
            log.error(
                f"Manager directory {self.dir} already exists but savefile "
                f"{self.saveFileName} does not exist! This suggests that "
                "either the savefile was manually deleted or the manager was "
                "not shut down properly. If you want to continue from the last "
                f"known state, create a softlink {self.saveFileName} to latest "
                f"savefile in the {self.dir}, either {self.saveFileName}.latest "
                f"or {self.saveFileName}.YYYYMMDD_HHMM_SS, if the .latest is "
                "corrupted. If you want to start from scratch, delete the "
                f"manager directory {self.dir} and start a new manager."
            )
            raise FileExistsError

        return True, "n"  # automatically assume new

    def ask_for_message(self) -> None:
        """Asks user for a message to be saved in the save file for bookkeeping."""

        log.info("Enter a message to be saved in the save file " "for bookkeeping.")
        i, o, e = select.select([sys.stdin], [], [], 60)
        if i:
            self.mgrMsg = sys.stdin.readline().strip()

    def add_job(self, j: job, update: bool = False) -> None:
        """Adds a job to the manager. If the job already exists and `update` is
        `True`, it will be updated.

        Arguments:
            j (job): job to be added
            update (bool, optional): whether to update the job if it already
            exists. Defaults to False.
        """
        # some reserved names, to simplify saving later
        if j.name in manager.reservedNames:
            log.error("Name %s  is reserved! Exiting ...", j.name)
            raise SystemExit

        # first check if the jobs already exists
        if j.name in self.jobs.keys():
            if not update:
                log.error("Job %s already exists! Exiting ...", j.name)
                raise SystemExit
            else:
                log.info(f"Updating job {j.name}.")

        self.jobs[j.name] = j

    def save(self, quiet: bool = False) -> None:
        """Saves the current status of the jobs to a json file.

        If `quiet` is `True`, it will not print any messages and
        will not make a time-stamped copy of the save file.

        Arguments:
            quiet (bool, optional): whether to print messages. Defaults to False.
        """
        if not quiet:
            log.info("Saving current status of jobs")
        output: Dict[str, Any] = {
            "Message": self.mgrMsg,
            "Command": self.command,
        }
        for name, j in self.jobs.items():
            output[name] = j.save()

        # save with a timestamp as a suffix, create sym link
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M_%S")
        fileLatest = f"{self.saveFileName}.latest"
        fileSuf = f"{self.saveFileName}.{current_time}"  # only if not quiet

        with open(fileLatest, "w") as f:
            json.dump(output, f, indent=2)
        if not quiet:
            log.info("Success! Making copy with time-stamp.")
            log.debug(f"Time-stamped file: {fileSuf}")
            if not os.path.exists(fileSuf):
                shutil.copyfile(fileLatest, fileSuf)
            else:
                raise FileExistsError(
                    f"Destination file {fileSuf} already exists. "
                    "This should not be possible."
                )

        # not necessary to remove, but maybe better to be sure its not broken
        if os.path.exists(self.saveFileName):
            os.remove(self.saveFileName)
        os.symlink(fileLatest.split("/")[-1], self.saveFileName)

        # clean up old save files
        files = glob(f"{self.saveFileName}.*")
        # sort based on time-stamp
        files.sort()
        # Here -1 because of the `latest`
        files = files[: -self.keepSaveFiles - 1]
        for fl in files:
            log.debug(f"Removing old save file {fl}")
            os.remove(fl)

    def load(self, retryFailed: bool = False) -> None:
        """Loads the saved status of the jobs from a json file
        provided by the user.

        Arguments:
            retryFailed (bool, optional): whether to retry the failed jobs.
            Defaults to False.
        """
        log.info("Loading past status of jobs")
        with open(self.dir + "/data.json", "rb") as f:
            depNames = {}
            for name, jobDict in ijson.kvitems(f, ""):
                if name in manager.reservedNames:
                    continue
                log.debug("Loading job %s", name)

                # create a job
                j = job(name, self.schedd)
                j.load(jobDict)

                # add it to the manager
                self.add_job(j, update=True)

                # decorate the list of names of the dependencies
                depNames[j.name] = jobDict["depNames"]

        # Now that jobs are defined, dependencies can be recreated
        # also resubmit jobs which failed
        for j in self.jobs.values():
            dependencies = [self.jobs[name] for name in depNames[j.name]]
            j.add_job_dependency(*dependencies)

        # Retry failed jobs
        # Since this changes the status and submits
        # jobs, add safequard in case of crash
        # to save up-to-date state
        if retryFailed:
            try:
                for j in self.jobs.values():
                    self._check_resubmit(j, True)
            except KeyboardInterrupt:
                log.error("Manager interrupted with keyboard!")
                log.error("Saving and exitting ...")
                self.save()
                self.print_failed()
                sys.exit(0)
            except Exception:
                log.error("Error ocurred when running manager!")
                traceback.print_exc(file=sys.stdout)
                self.save()
                self.print_failed()
                sys.exit(1)

    # print names of all failed jobs
    def print_running(self, printLogs: bool = False) -> None:
        log.info("Printing running jobs:")
        for name, j in self.jobs.items():
            if j.get_status() == FalconryStatus.RUNNING:
                log.info(f"{name} (id {j.jobID})")
                if printLogs:
                    log.info(f"log: {j.logFile}")
                    log.info(f"out: {j.outFile}")
                    log.info(f"err: {j.errFile}")

    # print names of all failed jobs
    def print_failed(self, printLogs: bool = False) -> None:
        """Prints names of all failed jobs.

        Arguments:
            printLogs (bool, optional): whether to print paths to logs.
                Defaults to False.
        """
        log.info("Printing failed jobs:")
        for name, j in self.jobs.items():
            if j.get_status() == FalconryStatus.FAILED:
                log.info(f"{name} (id {j.jobID})")
                if printLogs:
                    log.info(f"log: {j.logFile}")
                    log.info(f"out: {j.outFile}")
                    log.info(f"err: {j.errFile}")
        # TODO: maybe separate failed and removed?
        log.info("Printing removed jobs:")
        for name, j in self.jobs.items():
            if j.get_status() == FalconryStatus.REMOVED:
                log.info(f"{name} (id {j.jobID})")
                if printLogs:
                    log.info(f"log: {j.logFile}")
                    log.info(f"out: {j.outFile}")
                    log.info(f"err: {j.errFile}")

    def _check_dependence(self) -> None:
        """Checks if all dependencies of a job are done. If so, it will submit
        the job. If any of the dependencies failed, it will add the job to the
        skipped list.
        """

        # TODO: consider if not submitted jobs in a special list
        for name, j in self.jobs.items():
            # only check jobs which are neither submitted nor skipped
            if j.submitted or j.skipped:
                continue

            # if ready submit, single not done dependency leads to isReady=False
            isReady = True
            for tarJob in j.dependencies:
                # if any job is not done, do not submit
                if tarJob.done:
                    continue

                isReady = False

                if tarJob.skipped or tarJob.failed:
                    log.error(
                        f"Job {name} depends on job {tarJob.name} which either failed or was skipped! Skipping ..."
                    )
                    j.skipped = True

                status = tarJob.get_status()
                if status == FalconryStatus.REMOVED:
                    log.error(
                        f"Job {name} depends on job {tarJob.name} which is {FalconryStatus.REMOVED}! Skipping ..."
                    )
                    j.skipped = True

                break

            if isReady:
                # Check if we did not reach maximum number of submitted jobs
                if self.maxJobIdle != -1 and self.curJobIdle > self.maxJobIdle:
                    break  # break because it does not make sense to check any other jobs now
                j.submit(doNotSubmit=True)
                self.sub_queue.append(j)
                self.curJobIdle += 1  # Add the jobs as a idle for now

    def _check_resubmit(self, j: job, retryFailed: bool = False) -> None:
        """Checks if a job should be resubmitted due to some known problems.

        Arguments:
            j (job): job to check
            retryFailed (bool, optional): whether to also retry failed jobs.
                Defaults to False.
        """
        status = j.get_status()
        log.debug("Job %s has status %s", j.name, status.name)
        if status is FalconryStatus.ABORTED_BY_USER:
            log.warning(
                f"Error! Job {j.name} (id {j.jobID}) failed due to condor, rerunning"
            )
            j.submit(force=True, doNotSubmit=True)
            self.sub_queue.append(j)
        elif retryFailed and status is FalconryStatus.FAILED:
            log.warning(
                f"Error! Job {j.name} (id {j.jobID}) failed and will be retried, rerunning"
            )
            j.submit(force=True, doNotSubmit=True)
            self.sub_queue.append(j)
        elif retryFailed and status is FalconryStatus.REMOVED:
            log.warning(
                f"Error! Job {j.name} (id {j.jobID}) was removed and will be retried, rerunning"
            )
            j.submit(force=True, doNotSubmit=True)
            self.sub_queue.append(j)
        elif (
            retryFailed
            and j.submitted
            and (
                status
                in [FalconryStatus.NOT_SUBMITTED, FalconryStatus.LOG_FILE_MISSING]
            )
        ):
            log.warning(
                f"Error! Job {j.name} was not submitted succesfully (probably...), rerunning"
            )
            j.submit(force=True, doNotSubmit=True)
            self.sub_queue.append(j)
        elif retryFailed and j.skipped:
            log.warning(
                f"Error! Job {j.name} was skipped and will be retried, rerunning"
            )
            j.skipped = False

    def _count_jobs(self, counter: Counter) -> None:
        """Counts the number of jobs with different status.
        Resubmits jobs which failed due to condor problems.

        Arguments:
            c (counter): counter object to count the jobs
        """

        def _fit_to_width(text: str, width: int) -> str:
            if len(text) <= width:
                return text
            return text[: width - 1] + "…"

        termWidth = shutil.get_terminal_size(fallback=(80, 24)).columns
        clearLine = " " * termWidth + "\r"
        for name, j in self.jobs.items():
            printStr = _fit_to_width(f"Checking {name}\r", termWidth)
            print(printStr, end='', flush=True)
            self._count_job(counter, j)
            print(clearLine, flush=True, end='')

    def _count_job(self, c: Counter, j: job) -> None:
        """Updates the counter object with the status of a single job.
        Also resubmits jobs which failed due to condor problems.

        Arguments:
            c (counter): counter object to update
            j (job): job to check
        """

        # first check if job is not submitted, skipped or done
        if j.skipped:
            c.skipped += 1
            return
        if not j.submitted:
            c.waiting += 1
            return
        if j.done:
            c.done += 1
            return

        #  resubmit job which failed due to condor problems
        self._check_resubmit(j)

        # count job with different status
        status = j.get_status()
        if (
            status == FalconryStatus.NOT_SUBMITTED
            or status == FalconryStatus.LOG_FILE_MISSING
        ):
            c.notSub += 1
        elif status == FalconryStatus.IDLE:
            c.idle += 1
        elif status == FalconryStatus.RUNNING:
            c.run += 1
        elif status == FalconryStatus.FAILED:
            c.failed += 1
        elif status == FalconryStatus.COMPLETE:
            c.done += 1
        elif status == FalconryStatus.HELD:
            c.held += 1
        elif status == FalconryStatus.REMOVED:
            c.removed += 1

    def _submit_jobs(self) -> None:
        """Submits all jobs in the submission queue."""

        if len(self.sub_queue) == 0:
            return

        # First we need to group jobs with the same executable
        jobs_with_exe: Dict[str, list[job]] = {}
        for j in self.sub_queue:
            exe = j.config["executable"]
            if exe not in jobs_with_exe:
                jobs_with_exe[exe] = []
            # check that the log path is the same. This should be the case by default
            elif j.config["log"] != jobs_with_exe[exe][0].config["log"]:
                log.error("Jobs with same executable have different log paths")
                raise Exception
            jobs_with_exe[exe].append(j)

        ignore = ["executable", "log", "output", "error"]
        # Now we need to submit each group
        for exe, jobs in jobs_with_exe.items():
            #
            log.debug("Submitting %i jobs with executable %s", len(jobs), exe)

            job_pars = [x.config for x in jobs]
            all_pars = set(sum([list(x.keys()) for x in job_pars], []))

            def var_name(x: str) -> str:
                return f"VAR_{x}".replace("+", "p")

            pars_dict = {x: f'$({var_name(x)})' for x in all_pars if x not in ignore}
            job_pars_variable = []
            for par in job_pars:
                tmp = {}
                for k, v in par.items():
                    if k not in ignore:
                        tmp[var_name(k)] = v
                job_pars_variable.append(tmp)

            base_pars = {
                "executable": exe,
                "log": jobs[0].config["log"],
                "output": jobs[0].config["output"],
                "error": jobs[0].config["error"],
            }
            base_pars.update(pars_dict)
            base_submit = htcondor.Submit(base_pars)
            result = self.schedd.submit(base_submit, itemdata=iter(job_pars_variable))

            log.debug(f"Submitted cluster ID: {result.cluster()}")
            for it, j in enumerate(jobs):
                j.submit_done(result.cluster(), str(it))
        self.sub_queue = []

    def _start_cli(self, sleep_time: int = 60) -> None:
        """Starts the manager, iteratively checking status of jobs.

        Arguments:
            sleep_time (int, optional): time to sleep between checks.
                Defaults to 60.
        """
        # TODO: maybe add flag to save for each check? or every n-th check?

        log.info("MONITOR: START")

        c = Counter()
        event_counter = 0

        self._submit_jobs()

        while True:
            if not self._single_check(c):
                self._submit_jobs()
                break

            self._submit_jobs()

            # save with timestamp every 30 events
            # most important for first event when first
            # batch of jobs is defined
            if event_counter % 30 == 0:
                self.save()
            event_counter += 1

            if not self._cli_interface(sleep_time):
                break

        log.info("MONITOR: FINISHED")

    def _single_check(self, c: Counter) -> bool:
        """Single check in the manager loop.

        Returns:
            bool: True if manager should continue, False otherwise
        """
        log.info(
            f"|-Checking status of jobs [{datetime.datetime.now()}]----------------|",
        )

        cOld = copy.copy(c)
        c.reset()
        self._count_jobs(c)

        # if no job is waiting nor running, finish the manager
        if not (c.waiting + c.notSub + c.idle + c.run > 0):
            return False

        # only printout if something changed:
        if c != cOld:
            sleep(0.2)  # the printing sometimes breaks here, adding delay helps...
            log.info(
                "| nsub: {0:>4} | hold: {1:>5} | fail: {2:>6} | rem: {3:>6} | skip: {4:>5} |".format(
                    c.notSub, c.held, c.failed, c.removed, c.skipped
                )
            )
            log.info(
                "| wait: {0:>6} | idle: {1:>4} | RUN: {2:>5} | DONE: {3:>6} | TOT: {4:>6} |".format(
                    c.waiting, c.idle, c.run, c.done, len(self.jobs)
                )
            )

            # Update current idle of jobs managed by manager.
            # All new jobs submitted jobs in `check_dependence`
            # will increase this number, that why we create different
            # variable than `c.idle`
            self.curJobIdle = c.idle

            # checking dependencies and submitting ready jobs
            self._check_dependence()
            self.save(quiet=True)

            # instead of sleeping wait for input
            log.info(
                "|-Enter 'h' to show all commands, e.g. to resubmit or show failed jobs|"
            )

        return True

    def _cli_interface(self, sleep_time: int = 60) -> bool:
        """CLI interface for the manager.

        Possible commands:
            f: show failed jobs
            ff: show failed jobs and log paths
            s: save manager state
            r: show running jobs
            rr: show running jobs and log paths
            x: exit
            h: help


        Arguments:
            sleep_time (int, optional): time to sleep between checks.
                Defaults to 60.

        Returns:
            bool: True if manager should continue, False otherwise
        """
        print('>>>> ', end='', flush=True)
        state, var = cli.input_checker(
            {
                "h": "",
                "s": "",
                "f": "",
                "x": "",
                "ff": "",
                "retry all": "",
                "r": "",
                "rr": "",
            },
            silent=True,
            timeout=sleep_time,
        )
        if state == cli.InputState.TIMEOUT:
            print('\r    \r', end='', flush=True)
        elif state == cli.InputState.SUCCESS:
            if var == "f":
                self.print_failed()
            elif var == "s":
                self.save()
            elif var == "h":
                log.info(
                    "|-Enter 'f' to show failed jobs, 'ff' to also show log paths----------|"
                )
                log.info(
                    "|-Enter 'r' to show running jobs, 'rr' to also show log paths---------|"
                )
                log.info(
                    "|-Enter 'x' to exit, 's' to save or 'retry all' to retry all failed---|"
                )
                self._cli_interface(sleep_time)
            elif var == "ff":
                self.print_failed(True)
            elif var == "r":
                self.print_running()
            elif var == "rr":
                self.print_running(True)
            elif var == "x":
                log.info("MONITOR: EXITING")
                return False
            elif var == "retry all":
                for j in self.jobs.values():
                    self._check_resubmit(j, True)

        return True

    def _start_gui(self, sleepTime: int = 60) -> None:
        """Starts the manager with GUI, iteratively checking status of jobs.

        This is only experimental!

        Arguments:
            sleepTime (int, optional): time to sleep between checks.
                Defaults to 60.
        """

        log.warning("GUI version is only experimental!")
        import tkinter as tk

        window = tk.Tk()
        window.title("Falconry monitor")
        frm_counter = tk.Frame()

        def quick_label(name: str, x: int, y: int = 0) -> tk.Label:
            lbl = tk.Label(master=frm_counter, width=10, text=name)
            lbl.grid(row=y, column=x)
            return lbl

        quick_label("Not sub.:", 0)
        quick_label("Idle:", 1)
        quick_label("Running:", 2)
        quick_label("Failed:", 3)
        quick_label("Done:", 4)
        quick_label("Waiting:", 5)
        quick_label("Skipped:", 6)
        quick_label("Removed:", 7)
        labels = {}
        labels["ns"] = quick_label("0", 0, 1)
        labels["i"] = quick_label("0", 1, 1)
        labels["r"] = quick_label("0", 2, 1)
        labels["f"] = quick_label("0", 3, 1)
        labels["d"] = quick_label("0", 4, 1)
        labels["w"] = quick_label("0", 5, 1)
        labels["s"] = quick_label("0", 6, 1)
        labels["rm"] = quick_label("0", 1)

        frm_counter.grid(row=0, column=0)

        def tk_count() -> None:
            c = Counter()
            self._count_jobs(c)
            labels["ns"]["text"] = f"{c.notSub}"
            labels["i"]["text"] = f"{c.idle}"
            labels["r"]["text"] = f"{c.run}"
            labels["f"]["text"] = f"{c.failed}"
            labels["d"]["text"] = f"{c.done}"
            labels["w"]["text"] = f"{c.waiting}"
            labels["s"]["text"] = f"{c.skipped}"
            labels["rm"]["text"] = f"{c.removed}"

            # if no job is waiting nor running, finish the manager
            # TODO: add condition (close on finish)
            # if not (c.waiting + c.notSub + c.idle + c.run > 0):
            #    window.destroy()

            # checking dependencies and submitting ready jobs
            self._check_dependence()

            window.after(1000 * sleepTime, tk_count)

        tk_count()
        log.info("MONITOR: START")
        window.mainloop()
        log.info("MONITOR: FINISHED")

    def start(self, sleepTime: int = 60, gui: bool = False) -> None:
        """Starts the manager, iteratively checking status of jobs.

        Makes sure to save the current state of jobs
        in case of interupt or crash.

        Arguments:
            sleepTime (int, optional): time to sleep between checks.
                Defaults to 60.
            gui (bool, optional): whether to use GUI. Defaults to False.
                GUI is experimental!
        """
        try:
            if gui:
                self._start_gui(sleepTime)
            else:
                self._start_cli(sleepTime)
        except KeyboardInterrupt:
            log.error("Manager interrupted with keyboard!")
            log.error("Saving and exitting ...")
            self.save()
            self.print_failed()
            sys.exit(0)
        except Exception as e:
            log.error("Error ocurred when running manager!")
            log.error(str(e))
            traceback.print_exc(file=sys.stdout)
            self.save()
            self.print_failed()
            sys.exit(1)

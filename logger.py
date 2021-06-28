from datetime import date
from datetime import datetime
import pathlib
import arrow
import os
import traceback

pathlib.Path("logs").mkdir(parents=True, exist_ok=True)
logfilename = "errlog_" + date.today().strftime("%d%m%Y") + ".log"
logfile = open(str(pathlib.Path().resolve()) + "/logs/" + logfilename, "a")
logfile.write("Open date: " + datetime.now().strftime("%d/%m/%Y - %H:%M:%S") + "\n")

def clear_old_logs():
    path = pathlib.Path().resolve()
    path = pathlib.Path(str(path) + "\\logs")
    cutoffTime = arrow.now().shift(days=-30)
    for log in pathlib.Path(path).glob("*"):
        itemTime = arrow.get(log.stat().st_mtime)
        if itemTime < cutoffTime:
            os.remove(os.path.join(path, str(log)))

async def set_error(type, err):
    logfile.write("--ERROR TYPE: " + type + "--\n")
    logfile.write(err + "\n")

def set_error_offline(type, err):
    logfile.write("--ERROR TYPE: " + type + "--\n")
    logfile.write(err + "\n")

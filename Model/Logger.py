import logging

class Logger:

    logfile_name = ""

    logger = None

    def __init__(self, logfile_name):
        self._logger = logging.getLogger(__name__)
        self._logfile_name = logfile_name

    def initialize(self):
        self._logger.setLevel(logging.INFO)
        handler = logging.FileHandler(f"{self._logfile_name}.log", mode="a")
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
    def getlogfile_name(self):
        return self.logfile_name

    def getlogger(self):
        return self._logger


    logfile_name = property(getlogfile_name)
    logger = property(getlogger)


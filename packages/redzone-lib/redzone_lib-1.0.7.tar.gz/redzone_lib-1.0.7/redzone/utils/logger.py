from microgue.loggers.logger import Logger as _Logger

from ..settings import PROJECT_NAME


class Logger(_Logger):
    pass


logger = Logger(PROJECT_NAME)

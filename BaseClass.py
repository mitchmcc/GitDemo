import inspect
import logging


class BaseClass:

    @property
    def get_logger(self):
        # get name of caller off of stack to use for logging
        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)

        log_file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")
        log_file_handler.setFormatter(formatter)
        logger.addHandler(log_file_handler)
        logger.setLevel(logging.INFO)                         # TODO: change to method
        return logger

    """
        def set_level(self, level):
        logger.setLevel(level)
    """

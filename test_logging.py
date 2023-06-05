import logging


def test_logging_demo():
    logger = logging.getLogger(__name__)
    log_file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")
    log_file_handler.setFormatter(formatter)
    logger.addHandler(log_file_handler)
    logger.setLevel(logging.INFO)

    logger.debug("like a print statement")
    logger.info("print info message")
    logger.warning("watch out!")
    logger.error("okay, this is really bad")
    logger.critical("STOP THE PRESSES")

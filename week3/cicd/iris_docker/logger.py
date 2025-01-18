import logging
import os
import sys

def build_logger():
    """
    logger for FastAPI app
    """

    logger = logging.getLogger(__name__)
    handlers = logger.handlers[:]
    for handler in handlers:
        handler.close()
        logger.removeHandler(handler)
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt = "%(asctime)s %(levelname)-8s %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
    )

    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    
    logger.addHandler(stream_handler)
    logger.propagate = False

    return logger
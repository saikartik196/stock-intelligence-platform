from loguru import logger
import sys


def setup_logger(level: str = "INFO"):
    logger.remove()
    logger.add(sys.stdout, level=level)
    return logger

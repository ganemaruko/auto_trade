import logging
import os.path
from logging.handlers import RotatingFileHandler


def get_my_logger(name: str) -> logging.Logger:
    """Get the logger for the current module.

    Args:
        name (str): The name of the module.
    """
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s %(levelname)7s %(message)s')

    # add file handler.
    file_handler = RotatingFileHandler(
        os.path.join(os.path.dirname(__file__), './../../log/trade.log'),
        mode="a",
        encoding='utf-8',
        maxBytes=1000000
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # add std handler.
    std_handler = logging.StreamHandler()
    std_handler.setFormatter(formatter)
    logger.addHandler(std_handler)

    # set level.
    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    logger_ = get_my_logger(__name__)
    logger_.debug('debug')
    logger_.info('info')
    logger_.warning('warning')
    logger_.error('error')
    logger_.critical('critical')

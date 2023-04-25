import logging


def create_logger(name: str):
    """Logger wrapper for this library.

    Args:
        name: logger name. usually, used '__name__'.

    Examples:
        >>> _logger = create_logger(__name__)
        >>> _logger.info("example log.")

    References:
        https://docs.python.org/ja/3/howto/logging.html

    Returns:
        configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == '__main__':
    logger_ = create_logger(__file__)
    logger_.debug("sample message.")
    logger_.info("sample message.")
    logger_.error("sample message.")
    logger_.critical("sample message.")

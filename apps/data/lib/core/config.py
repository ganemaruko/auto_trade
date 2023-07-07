from functools import lru_cache

import yaml

from lib.core.logger import get_my_logger

logger = get_my_logger(__name__)


def _read_yaml(file_name: str) -> dict:
    """Read yaml file.

    Args:
        file_name: yaml file name.

    Returns:
        config: yaml file.
    """
    with open(f'./../../config/{file_name}.yml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config


@lru_cache(maxsize=None)
def db_info():
    """Get database information.

    Returns:
        config: database information.
    """
    logger.info("read db info.")
    config = _read_yaml("config")
    logger.info(f"db {config['database']=}")
    return config['database']


if __name__ == '__main__':
    print(db_info())

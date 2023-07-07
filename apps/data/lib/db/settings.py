from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from lib.core.config import db_info
from lib.core.logger import get_my_logger

logger = get_my_logger(__name__)


@lru_cache(maxsize=None)
def db_connection_string():
    """Get the connection string for the database.

    Notes:
        - This function is used to get the connection string for the database.
        - The connection string is cached using the lru_cache decorator, so this function is not named by verb.

    Raises:
        NotImplementedError: If the database_type is not implemented.

    Returns:
        str: The connection string for the database.
    """
    info = db_info()
    try:
        database_type = info['database_type']
    except KeyError as e:
        raise ValueError("The database_type is not set in the config file. Please see config/config.yml.") from e

    if database_type == 'mysql':
        return f"mysql+mysqlconnector://{info['user']}:{info['password']}@{info['host']}:{info['port']}/{info['database_name']}"
    else:
        raise NotImplementedError(f"database_type: {info['database_type']} is not implemented.")


path = db_connection_string()
logger.info(f"Create SqlAlchemy Base. db_connection_string: {path}.")

# Engine の作成
Engine = create_engine(
    path,
    # encoding="utf-8",
    echo=False
)

Base = declarative_base()

if __name__ == '__main__':
    pass

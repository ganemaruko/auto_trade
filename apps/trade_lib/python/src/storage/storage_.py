"""export implementation for storage"""
from typing import Any

from src.core.config import read_config
from src.storage.conoha.storage import ConohaStorage
from src.storage.storage_interface import StorageInterface
from src.core.logger import create_logger

logger = create_logger(__file__)


class StorageConfigure(StorageInterface):
    _instance: Any
    _storage_impl: StorageInterface

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(StorageConfigure, cls).__new__(cls)
            # configure storage type and setting on read storage module.
            config_file_name = "env.yml"  # noqa
            try:
                storage_config = read_config(config_file_name)["storage"]
                if storage_config["type"] == "conoha":
                    cls._storage_impl = ConohaStorage(**storage_config["configs"])
                else:
                    logger.info(f"can not read 'type' in your config {config_file_name}, use type = 'local'")
            except KeyError:
                import traceback
                logger.info(traceback.format_exc())
                logger.warn(f"your {config_file_name} has appropriate key.")

            return cls._instance
        else:
            return cls._instance

    def create(self, from_: str, to: str):
        self._storage_impl.create(from_, to)

    def read(self, from_: str, to: str):
        self._storage_impl.read(from_, to)

    def update(self, from_: str, to: str):
        self._storage_impl.update(from_, to)

    def delete(self, path: str):
        self._storage_impl.delete(path)


def create(from_: str, to: str):
    StorageConfigure().create(from_, to)


def read(from_: str, to: str):
    StorageConfigure().read(from_, to)


def update(from_: str, to):
    StorageConfigure().update(from_, to)


def delete(path: str):
    StorageConfigure().delete(path)


if __name__ == '__main__':
    a = create("tests.html", "public/tests.html")
    a = read("tests/sample.json", "read.json")
    a = delete("tests/sample.json")
    # a = create("sample", {})
    # a = create("sample", {})

from abc import ABC


class StorageInterface(ABC):
    @classmethod
    def update(cls, path: str):
        raise NotImplementedError()

    @classmethod
    def delete(cls, path: str):
        raise NotImplementedError()

    @classmethod
    def create(cls, path: str, obj):
        raise NotImplementedError()

    @classmethod
    def read(cls, path: str):
        raise NotImplementedError()

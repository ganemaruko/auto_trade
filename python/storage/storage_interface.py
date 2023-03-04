from abc import ABC


class StorageInterface(ABC):
    @classmethod
    def update(cls, from_: str, to: str):
        raise NotImplementedError()

    @classmethod
    def delete(cls, path: str):
        raise NotImplementedError()

    @classmethod
    def create(cls, from_: str, to: str):
        raise NotImplementedError()

    @classmethod
    def read(cls, from_: str, to: str):
        raise NotImplementedError()

from python.storage.storage_interface import StorageInterface


class ConohaStorage(StorageInterface):

    @classmethod
    def update(cls, path: str):
        pass


    @classmethod
    def delete(cls, path: str):
        raise NotImplementedError()

    @classmethod
    def create(cls, path: str, obj):
        raise NotImplementedError()

    @classmethod
    def read(cls, path: str):
        raise NotImplementedError()

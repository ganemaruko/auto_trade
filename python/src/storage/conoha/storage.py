import os.path
from typing import Optional

import paramiko
from paramiko.ssh_exception import BadHostKeyException, BadAuthenticationType, SSHException

from src.storage.storage_interface import StorageInterface
from src.core.logger import create_logger

logger = create_logger(__file__)


class ConohaStorage(StorageInterface):
    def __init__(self,
                 host: str,
                 username: str,
                 from_root: str,
                 to_root: str,
                 password: Optional[str] = None,
                 key_filename: Optional[str] = None,
                 port: int = 22,
                 ):
        self.host = host
        self.username = username
        self.password = password
        self.from_root = from_root
        self.to_root = to_root
        self.key_filename = key_filename
        self.port = port

    def connect(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        try:
            client.connect(self.host,
                           key_filename=self.key_filename,
                           port=self.port,
                           username=self.username,
                           password=self.password
                           )
            return client
        except BadHostKeyException as e:
            logger.error(
                "The host key given by the SSH server did not match what we were expecting."
            )
            raise e
        except BadAuthenticationType as e:
            logger.error(
                "Exception raised when an authentication type is used, but the server isn’t allowing that type."
            )
            raise e
        except SSHException as e:
            logger.error(
                "Exception raised by failures in SSH2 protocol negotiation or logic errors."
            )
            raise e

    def get_full_path_local(self, path: str) -> str:
        """Create full path.
        Args:
            path: such as "test/sample.json"

        Returns:
            str such as "/home/c0000000/public_html/DOMAIN/test/sample.json
        """
        return os.path.join(self.from_root, path)

    def get_full_path_remote(self, path: str) -> str:
        r"""Create full path.

        Args:
            path: such as "test/sample.json".
            conoha server is linux, so please use "/", not "\".

        Returns:
            str such as "/home/c0000000/public_html/DOMAIN/test/sample.json
        """
        return f"{self.to_root}/{path}"

    def create(self, from_: str, to: str):
        """Upsert remote server file.

        Args:
            from_: local file path.
            to: remote file path.
        """
        with self.connect() as client:
            with client.open_sftp() as sftp:
                sftp.put(
                    localpath=self.get_full_path_local(from_),
                    remotepath=self.get_full_path_remote(to)
                )

    def read(self, from_: str, to: str):
        """Copy from remote server.

        Args:
            from_: remote server path.
            to: local server path.

        Warnings:
            this method override local file.
        """
        with self.connect() as client:
            with client.open_sftp() as sftp:
                sftp.get(
                    localpath=self.get_full_path_local(to),
                    remotepath=self.get_full_path_remote(from_)
                )

    def update(self, from_: str, to):
        """Update remote server file.

        Args:
            from_: local file path.
            to: remote file path.
        """
        with self.connect() as client:
            with client.open_sftp() as sftp:
                sftp.put(
                    localpath=self.get_full_path_local(from_),
                    remotepath=self.get_full_path_remote(to)
                )

    def delete(self, path: str):
        with self.connect() as client:
            with client.open_sftp() as sftp:
                sftp.remove(
                    path=self.get_full_path_remote(path)
                )

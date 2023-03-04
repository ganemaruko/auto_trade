import os

import yaml

from python.core.config import read_config
from python.util.performance import stop_watch


def check_cache_performance():
    length = 1000

    @stop_watch
    def on_cache():
        for _ in range(length):
            read_config("env.yml")

    @stop_watch
    def off_cache():
        for _ in range(length):
            with open(os.path.join(os.path.dirname(__file__), "..", "..", "..", "common", "configs", "env.yml")) as f:
                yaml.safe_load(f)

    on_cache()
    off_cache()


if __name__ == '__main__':
    # there is no diff...
    check_cache_performance()

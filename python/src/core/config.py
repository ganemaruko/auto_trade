import os

import yaml


def read_config(path: str) -> dict:
    if not hasattr(read_config, "_cache"):
        # run only the first call.
        read_config.cache = dict()

    if path in read_config.cache:
        return read_config.cache[path]
    else:
        with open(os.path.join(os.path.dirname(__file__), "../..", "..", "common", "configs", path)) as f:
            config = yaml.safe_load(f)
            read_config.cache[path] = config
            return config


if __name__ == '__main__':
    print(read_config("env.yml"))

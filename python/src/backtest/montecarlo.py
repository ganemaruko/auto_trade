import random
from typing import Optional

import pandas as pd


def montecarlo(series: pd.Series, *, seed: Optional[int] = None):
    if seed is not None:
        random.seed(seed)
    return random.choices(series,
                          k=series.size,

                          )


if __name__ == '__main__':
    s = pd.Series(range(10))
    print(montecarlo(s, seed=10))

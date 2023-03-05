import random

import pandas as pd


def montecarlo(series: pd.Series):
    return random.choices(series, k=series.size)


if __name__ == '__main__':
    s = pd.Series(range(10))
    print(montecarlo(s))

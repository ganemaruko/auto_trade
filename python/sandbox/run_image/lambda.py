"""
pseudo code for FaaS service.
"""
from env.env_ import Environment
from market.market_ import Market


def main():
    market = Market()

    env = Environment(
        market=market,


    )


if __name__ == '__main__':
    main()

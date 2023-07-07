from datetime import datetime

import pandas_datareader.data as web

f = web.DataReader("AAPL",
                   "av-daily",
                   start=datetime(2017, 2, 9),
                   end=datetime(2017, 5, 24),
                   api_key='2AHSU97ALX9I08T1'
                   )

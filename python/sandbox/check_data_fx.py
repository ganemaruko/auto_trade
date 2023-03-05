# まずはデータ取得に使うライブラリをimport
import pandas_datareader.data as web
import pandas as pd

df = web.DataReader('DEXJPUS', 'fred', start='2000-01-01')

print(df.to_csv())
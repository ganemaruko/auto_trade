# まずはデータ取得に使うライブラリをimport
import pandas_datareader.data as web

df = web.DataReader('DEXJPUS', 'fred', start='2000-01-01')
df = df.rename(columns={"DEXJPUS": "USDJPY"})
print(df.isna().sum())
df = df.interpolate()
print(df.isna().sum())
print(df.to_csv("./../data/sample/USDJPY.csv"))

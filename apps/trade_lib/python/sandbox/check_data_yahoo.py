import datetime
import pandas_datareader.data as web
start = datetime.date(2010,1,1)
end = datetime.date.today()

df = web.DataReader('9984.T', 'yahoo', start, end)
df.head()
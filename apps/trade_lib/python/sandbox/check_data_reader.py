import pandas_datareader as pdr
df = pdr.get_data_fred('GS10')
print(df)
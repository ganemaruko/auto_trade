import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../data/sample/USDJPY.csv", index_col="DATE")
    data = data.rename(columns={"USDJPY": "PRICE"})
    data["MV"] = data["PRICE"].rolling(window=10).mean()
    print(data)
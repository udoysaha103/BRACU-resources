import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

dataframe = pd.read_csv("data.csv")
print(type(dataframe["Date"][2]))

dataframe["DateConverted"] = pd.to_datetime(dataframe["Date"], format="mixed")
dataframe["ConvertedClose/Last"] = dataframe["Close/Last"].apply(lambda row: row[1:])

print(dataframe.head())

print(dataframe["DateConverted"][2])
print(dataframe["DateConverted"][2])
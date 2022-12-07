import pandas as pd
import numpy as np
import matplotlib as plt
file_loc = "dados.xlsx"

df = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols="C")


df1 = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols="G" )
#df1 = df1.iloc[1: , :]
print(df1)

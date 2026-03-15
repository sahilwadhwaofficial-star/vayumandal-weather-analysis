import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\sahil\Downloads\New folder (2)\pressure.csv")
print(df.isnull().sum())
df.interpolate(method = 'linear',inplace = True ,limit_direction = "both" )
print(df.isnull().sum())
#print(df.head())
df.to_csv("FINAL_pressure.csv",index=False)
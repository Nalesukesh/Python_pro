import pandas as pd

Data=pd.read_csv(r"C:\Users\nales\OneDrive\Desktop\50000 Sales Records.csv")
print(Data)
print(Data.shape)
print(Data.duplicated().sum())
print(len(Data))
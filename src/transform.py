import pandas as pd 

df = pd.read_csv("data/raw/carburants.csv", sep=";")

print("Nombre de ligne et de colone :  ", df.shape)
print(df.head())
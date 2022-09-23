import pandas as pd
import csv
df = pd.read_csv("final.csv")
del df["Luminosity"]
for index in df:
    if df[index] == "NAN":
        del df[index]
    if df[index] == df[index -1]:
        del df[index]

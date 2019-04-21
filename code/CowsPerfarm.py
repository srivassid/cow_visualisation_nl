import pandas as pd

raw_df = pd.read_csv("FarmsCows.csv",sep=";",usecols=["NumberofCows","NumberofFarms","Regions"])

df = pd.DataFrame(columns=["Regions","CowsPerFarm"])

for i,j,k,l in raw_df.itertuples():
    df.loc[i] = [j.split(" ")[0],int(k)/int(l)]

print(df.head())

df.to_csv("cowsPerFarm.csv",sep=",",header=True,index=False)
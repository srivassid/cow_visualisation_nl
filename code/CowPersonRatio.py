import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

raw_df = pd.read_csv("cow_data_2.csv", sep=';')

population = {'Zeeland':382304,'Groningen':582944,"Drenthe":492100,"Flevoland":411670, "Friesland":647268,"Gelderland":2060103,
              "Limburg":1117198,"Noord-Brabant":2528286,"Noord-Holland":2831182,"Overijssel":1151501,"Zuid-Holland":3681044,
              "Utrecht":1295484}

df = raw_df[['Regions','Grazing livestock/Number of animals/Cattle/Dairy cows (>= 2 years) (number)']]


df_2 = pd.DataFrame(columns=['Regions','CowsPerPerson'])

for i,j,k in df.itertuples():
    if j.split(" ")[0] in population.keys():
        df_2.loc[i] = [j.split(" ")[0],k/population[j.split(" ")[0]]]


df_2.to_csv("cows_per_person.csv",sep=",",header=True,index=False)


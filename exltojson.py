import pandas as pd
import json
import sys

# Read the csv

df = pd.read_csv("guwienko.csv", sep=";")

#get how many columns are in the csv
columns = len(df.columns)

data = {}

#df get first column from second row
df = df.iloc[1:,0]
#df to json variable
js = df.to_json(orient='records')
data["time"] = json.loads(js)

for i in range(1,columns):
    df = pd.read_csv("guwienko.csv", sep=";")
    gdf = df.iloc[1:,i]
    js = gdf.to_json(orient='records')
    try:
        data[df.iloc[0][i]][gdf.name.split(".")[0]] = json.loads(js)
    except:
        data[df.iloc[0][i]] = {}
        data[df.iloc[0][i]][gdf.name.split(".")[0]] = json.loads(js)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
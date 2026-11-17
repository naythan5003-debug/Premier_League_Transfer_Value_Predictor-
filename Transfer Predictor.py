import requests
url = 'https://api.football-data.org/v4/competitions/PL/scorers?limit=500'   

#get your free API token from football-data.org
headers = {
    'X-Auth-Token':"YOUR-API-TOKEN-HERE"
}
response = requests.get(url,headers=headers)
players = []
data = response.json()

for player in data['scorers']:
    name = player['player']['name']
    goals = player['goals']
    matches = player['playedMatches']
    assists = player['assists']

    if assists == None:
        assists = 0 
    players.append([name,matches,goals,assists])


import csv 

f = open('premier.csv','w',newline='',encoding='utf-8')
w = csv.writer(f)
w.writerow(['Name','Matches','Goals','Assists'])
for i in players:
    w.writerow(i)

f.close()
import pandas as pd
import unicodedata

def clean(s):
    return unicodedata.normalize('NFKD',str(s)).encode('ascii','ignore').decode().lower().strip()

f = pd.read_csv("players.csv.gz")
f['key'] = f['name'].apply(clean)
f = f.dropna(subset=['market_value_in_eur']).drop_duplicates('key')

final = [] 
for player in players:
      name = player[0]
      matches = player[1]
      goals = player[2]
      assists = player[3]

      result = f[f['key']==clean(name)]

      if len(result)>0:
       
       value = result['market_value_in_eur'].iloc[0]
       final.append([name,matches,goals,assists,value])
#print(final)
print(len(final),'players matched')     


import numpy as np
from sklearn.ensemble import RandomForestRegressor

X = [] 
Y = [] 
for i in final:
    X.append([i[1],i[2],i[3]])   #things we are using to predict 
    Y.append(np.log1p(i[4]))     #things we are trying to predict 
model = RandomForestRegressor(300,random_state=0)
model.fit(X,Y)

print('Model Trained')

matches = int(input("Enter matches: "))
goals = int(input("Enter goals: "))
assists = int(input("Enter assists: "))


mx = np.max(X,axis=0)
matches = min(matches,mx[0])
goals = min(goals,mx[1])
assists = min(assists,mx[2])

prediction = np.expm1(model.predict([[matches, goals, assists]]))

value = prediction[0]

if value >= 1000000:
    print("Predicted Market Value: €" + str(round(value/1000000,1)) + " million")
else:
    print("Predicted Market Value: €" + str(round(value/1000)) + "k")


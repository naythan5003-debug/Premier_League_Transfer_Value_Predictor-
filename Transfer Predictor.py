import requests
url = 'https://api.football-data.org/v4/competitions/PL/scorers'
headers = {
    'X-Auth-Token':"API KEY"
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
#print(players)

import csv 

f = open('premier.csv','w',newline='')
w = csv.writer(f)
w.writerow(['Name','Matches','Goals','Assists'])
for i in players:
    w.writerow(i)

f.close()
import pandas as pd

f = pd.read_csv("C:/Users/Nayth/OneDrive/Desktop/Naythan/Premier_League/players.csv.gz")

final = [] 
for player in players:
      name = player[0]
      matches = player[1]
      goals = player[2]
      assists = player[3]

      result = f[f['name']==name]

      if len(result)>0:
       
       value = result['market_value_in_eur'].iloc[0]
       final.append([name,matches,goals,assists,value])
#print(final)

from sklearn.linear_model import LinearRegression 

X = [] 
Y = [] 
for i in final:
    X.append([i[1],i[2],i[3]])   #things we are using to predict 
    Y.append(i[4])   #things we are trying to predict 
model = LinearRegression()
model.fit(X,Y)

print('Model Trained')

matches = int(input("Enter matches: "))
goals = int(input("Enter goals: "))
assists = int(input("Enter assists: "))

prediction = model.predict([[matches, goals, assists]])

print("Predicted Market Value:",round(prediction[0]))


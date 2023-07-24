import requests, json, os
import pandas as pd

endpt_list = ['games', 'matches', 'tournaments']
"""
#GAMES
api_url = f'https://api.rivalry.com/api/v1/{endpt_list[0]}'
data = requests.get(api_url).json()
lst_pg = data['meta']['last_page']

id, names = [], []
for i in range(1, lst_pg + 1):
    base_url = f'https://api.rivalry.com/api/v1/{endpt_list[0]}?page={i}'
    data = requests.get(base_url).json()['data']
    
    for item in data:
        id.append(item['id'])
        names.append(item['name'])

zipped = list(zip(id, names))
df = pd.DataFrame(zipped, columns=['Game ID', 'Game Names'])
print(df)
"""

#GAMES for MLBB id 39
api_url = f'https://api.rivalry.com/api/v1/games/39'
data = requests.get(api_url).json()['data']['matches']


match_id, tournament_id, tournament_name = [], [], []
team1_id, team1_name, team2_id, team2_name = [], [], [], []
scheduled_at, offered_live, url = [], [], []

for item in data:
    match_id.append(item['id'])
    tournament_id.append(item['tournament']['id'])
    tournament_name.append(item['tournament']['name'])

    team1 = item['competitors'][0]
    for subitem in team1:
        team1_id.append(team1['id'])
        team1_name.append(team1['name'])
    
    team2 = item['competitors'][1]
    for subitem in team2:
        team2_id.append(team2['id'])
        team2_name.append(team2['name'])
    
    scheduled_at.append(item['scheduled_at'])
    offered_live.append(item['offered_live'])
    url.append(item['url'])

zipped = list(zip(match_id, tournament_id, tournament_name, team1_id, team1_name, team2_id, team2_name, scheduled_at, offered_live, url))
df = pd.DataFrame(zipped, columns=['Match ID',
                                   'Tournament ID',
                                   'Tournament Name',
                                   'Team1 ID',
                                   'Team1 Name',
                                   'Team2 ID',
                                   'Team2 Name',
                                   'Scheduled At',
                                   'Offered Live',
                                   'Url'])
df.to_csv('MLBB_data.csv', index=False)



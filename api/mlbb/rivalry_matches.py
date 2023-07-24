import requests, json, os
import pandas as pd

endpt_list = ['games', 'matches', 'tournaments']

#MATCHES
api_url = f'https://api.rivalry.com/api/v1/matches/'
data = requests.get(api_url).json()
lst_pg = data['meta']['last_page']

game_id, game_name, tournament, id, competitors, markets = [], [], [], [], [], [], []
scheduled_at, offered_live, url = [], [], []

for i in range(0, lst_pg + 1):
    base_url = f'https://api.rivalry.com/api/v1/matches?page={i}'
    data = requests.get(base_url).json()['data']
    
    for item in data:
        for subitem in item['game']:
            game_id.append(item['game'])  ##--> GET BACK HERE on separating game id and game name
        tournament.append(item['tournament'])
        #id.append(item['id'])
        #competitors.append(item['competitors'])
        #markets.append(item['markets'])
        #scheduled_at.append(item['scheduled_at'])
        #offered_live.append(item['offered_live'])
        #url.append(item['url'])

zipped = list(zip(game, tournament))
df = pd.DataFrame(zipped, columns=['Game', 'Tournament'])
print(df)
"""      
zipped = list(zip(game, tournament, id, competitors, markets, scheduled_at, offered_live, url))
df = pd.DataFrame(zipped, columns=['Game Name', 
                                    'Tournament Name',
                                    'Tournament ID',
                                    'Competitors',
                                    'Markets',
                                    'Scheduled At',
                                    'Offered Live',
                                    'Url'])

df.to_csv('matches_data.csv', index=False)
"""

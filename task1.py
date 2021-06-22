from urllib.request import urlopen
import json
import csv

match_id = 1237181


def GetDetails(match_id, file_name):
    url = f"https://www.espncricinfo.com/matches/engine/match/{match_id}.json"
    response = urlopen(url)
    data = json.loads(response.read())

    ground_id = data['match']['ground_id']
    date_string = data['match']['date_string']
    home_team_id = data['match']['home_team_id']
    if int(home_team_id) == 0:
        home_team_name = ""
    else:
        home_team_name = data['match']['home_team_name']
    away_team_id = data['match']['away_team_id']
    if int(away_team_id) == 0:
        away_team_name = ""
    else:
        away_team_name = data['match']['away_team_name']

    teams = data['team']
    i = 0
    rows = []
    for team in teams:
        players = team['player']
        team_id = team['team_id']
        team_name = team['team_name']
        for player in players:
            new = {}
            new['match_id'] = match_id
            new['date'] = date_string
            new['ground_id'] = ground_id
            new['home_team_id'] = home_team_id
            new['home_team_name'] = home_team_name
            new['away_team_id'] = away_team_id
            new['away_team_name'] = away_team_name
            new['player_name'] = player['known_as']
            new['player_id'] = player['object_id']
            new['team_id'] = team_id
            new['batting_style'] = player['batting_style']
            new['bowling_style'] = player['bowling_style']
            rows.append(new)

    return rows


rows = GetDetails(match_id, True)
keys = rows[0].keys()


with open(f'{match_id}.csv', 'w', newline="") as file:
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(rows)

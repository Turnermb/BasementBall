import requests
from random import randrange as random
import json


# Player Classes
class Player:
  def __init__(self, name, position, stats):
    self.name = name
    self.position = position
    self.stats = stats

# Gets random player name from random name API
def get_name():
    response = requests.get("https://randomuser.me/api/")
    response = response.json()
    json_string = json.dumps(response)
    json_dict = json.loads(json_string)

    name = json_dict['results'][0]['name']['first'] + " " + json_dict['results'][0]['name']['last']
    return name

# Generate Player Stats
def get_stats():
  player_stats = {"Pitching": 0, "Defense": 0, "Hitting": 0}
  pitching = random(1, 6)
  defense = random(1, 6)
  hitting = random(1, 6)
  player_stats["Pitching"] = pitching
  player_stats["Defense"] = defense
  player_stats["Hitting"] = hitting

  return player_stats

# Generate Teams Of Player Objects
def generate_team(team):
  for i in range(0, 9): #Creates 9 Player Objects With Random Stats Assigns Them To The Specified Team.
    name = get_name()
    player = Player(name, "Outfield", get_stats())
    team.append(player)


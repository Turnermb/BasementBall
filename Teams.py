import requests
from random import randrange as random
import json


# Player Classes
class Player:
  def __init__(self, name, stats, position):
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
  
  def get_stats(self):
    return self.stats
  
  def get_position(self):
    return self.stats


class Pitcher(Player):
  def __init__(self, name, stats, position = "Pitcher"):
    super().__init__(name, stats, position)
  
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
    

class Outfielder(Player):
  def __init__(self, name, stats, position = "Outfield"):
    super().__init__(name, stats, position)

  # Generate Player Stats
  def get_stats():
    player_stats = {"Defense": 0, "Hitting": 0}
    defense = random(1, 6)
    hitting = random(1, 6)
    player_stats["Defense"] = defense
    player_stats["Hitting"] = hitting

    return player_stats
  
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
  pitcher = Pitcher(get_name(), Pitcher.get_stats())
  team.append(pitcher)
  for i in range(0, 8): #Creates 9 Player Objects With Random Stats Assigns Them To The Specified Team.  
    fielder = Outfielder(Outfielder.get_name(), Outfielder.get_stats())
    team.append(fielder)


import requests
from random import randrange as random
import json
import time

# Current Basement Ball teams.
the_system = {"Name": "The System", "Score": 0, "Home Field": "Billionaire Row", "Players": []}
job_hunters = {"Name": "The Job Hunters","Score": 0, "Home Field": "Cubicle Park", "Players": []}

# Team class. Currently unused.
class Team:
  def __init__(self, name, score, home_field, players):
    self.name = name
    self.name = score
    self.home_field = home_field
    self.players = players

# Player classes.
class Player(Team):
  def __init__(self, name, stats, position):
    self.name = name
    self.stats = stats
    self.position = position

    # Gets random player name from random name API.
  def get_name():
    response = requests.get("https://randomuser.me/api/?inc=name,nat&nat=au,br,ca,ch,de,dk,es,fi,fr,gb,ie,in,mx,nl,no,nz,rs,tr,ua,us")
    response = response.json()
    json_string = json.dumps(response)
    json_dict = json.loads(json_string)

    name = json_dict['results'][0]['name']['first'] + " " + json_dict['results'][0]['name']['last']
    return name
  
  def get_stats(self):
    return self.stats
  
  def get_position(self):
    return self.position


class Pitcher(Player):
  def __init__(self, name, stats, position = "Pitcher"):
    super().__init__(name, stats, position)
  
  # Generate player stats.
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

  # Generate player stats.
  def get_stats():
    player_stats = {"Defense": 0, "Hitting": 0}
    defense = random(1, 6)
    hitting = random(1, 6)
    player_stats["Defense"] = defense
    player_stats["Hitting"] = hitting

    return player_stats

# Generate teams of Player objects.
def generate_team(team):

  pitcher = Pitcher(Pitcher.get_name(), Pitcher.get_stats())
  team["Players"].append(pitcher)
  for i in range(0, 8): #Creates 9 Player Objects With Random Stats Assigns Them To The Specified Team.  
    fielder = Outfielder(Outfielder.get_name(), Outfielder.get_stats())
    team["Players"].append(fielder)

generate_team(the_system)
generate_team(job_hunters)
import requests
from random import randrange as random
import json

# Current Basement Ball teams.

teams = (
  #{"Name": "The System", "Score": 0, "Wins": 0, "Losses": 0, "Division": "", "Hated Rival": "The Job Hunters", "Home Field": "Billionaire Row", "Players": []}, 
  #{"Name": "The Job Hunters","Score": 0, "Wins": 0, "Losses": 0, "Division": "", "Hated Rival": "The System", "Home Field": "Cubicle Park", "Players": []},
  #{"Name": "The Los Angeles Bagels", "Score": 0, "Wins": 0, "Losses": 0, "Division": "", "Hated Rival": "", "Home Field": "The O", "Players": []}
  {"Name": "The Amarillo Chanclas","Score": 0, "Wins": 0, "Losses": 0, "Division": "South", "Hated Rival": "The Nantucket Shoobies", "Home Field": "The Shoe", "Players": []},
  {"Name": "The Tallahassee Whippersnappers","Score": 0, "Wins": 0, "Losses": 0, "Division": "South", "Hated Rival": "The Red River Ladybugs", "Home Field": "Werther's Original Park", "Players": []},
  {"Name": "The Roanoke Underachievers","Score": 0, "Wins": 0, "Losses": 0, "Division": "East", "Hated Rival": "The Cheyenne Union", "Home Field": "The Substandard Dome", "Players": []},
  {"Name": "The Nantucket Shoobies","Score": 0, "Wins": 0, "Losses": 0, "Division": "East", "Hated Rival": "The Amarillo Chanclas", "Home Field": "The Sound", "Players": []},
  {"Name": "The Kalamazoo Troublemakers","Score": 0, "Wins": 0, "Losses": 0, "Division": "North", "Hated Rival": "The Pasadena Preachers", "Home Field": "The Schoolyard", "Players": []},
  {"Name": "The Red River Ladybugs","Score": 0, "Wins": 0, "Losses": 0, "Division": "North", "Hated Rival": "The Tallahassee Whippersnappers", "Home Field": "Red River Field", "Players": []},
  {"Name": "The Pasadena Preachers","Score": 0, "Wins": 0, "Losses": 0, "Division": "West", "Hated Rival": "The Kalamazoo Troublemakers", "Home Field": "The Pulpit", "Players": []},
  {"Name": "The Cheyenne Union","Score": 0, "Wins": 0, "Losses": 0, "Division": "West", "Hated Rival": "The Roanoke Underachievers", "Home Field": "Union Station", "Players": []}
)

# Player classes.
class Player():
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

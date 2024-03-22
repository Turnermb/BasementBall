# Basement Ball
# What is required to make a baseball game work at the most basic level.

from random import randrange as random
import time


# Teams
job_hunters = []
the_system = []

# Players
  
# Player Class
class Player:
  def __init__(self, name, position, stats):
    self.name = name
    self.position = position
    self.stats = stats

# Generate Player Stats
def stat_generator():
  player_stats = {"Pitching": 0, "Defense": 0, "Hitting": 0}
  pitching = random(1, 5)
  defense = random(1, 5)
  hitting = random(1, 5)
  player_stats["Pitching"] = pitching
  player_stats["Defense"] = defense
  player_stats["Hitting"] = hitting

  return player_stats

# Generate Teams Of Player Objects
def generate_teams():
  for i in range(0, 18): #Creates 18 Player Objects With Random Stats And Separates Them Into Two Teams
    player = Player("Player" + str(i+1), "Outfield", stat_generator())
    if len(job_hunters) < 9:
      job_hunters.append(player)
    elif len(job_hunters) >= 9:
      the_system.append(player)

generate_teams()

# At bat
    # (hitting level * 10) - (pitching level * 3) > math.random(100) = hit else strikes += 1.
    # if strikes < 3 continue else outs += 1.
    # if outs < 3 continue else change team[i + 1].
    # if team[2] innings += 1.

score = {"THE JOB HUNTERS": 0, "THE SYSTEM": 0}

def play_game():
  inning = 1
  for i in range(0, 8):
    print("INNING:", inning, "\n")
    play_inning()
    inning += 1
    
  print("THAT'S THE GAME!")
  print(score)
  
def play_inning(): # Plays one inning of baseball
  outs = 0
  hits = 0
  i = 0
  print("NOW PITCHING: ", str(the_system[0].name), " ", str(the_system[0].stats), "\n")
  # Home At Bat
  while outs < 3:
    time.sleep(1.5)
    if at_bat_home(i) == "Hit":
      hits += 1
      if hits > 3:
        print("A RUN SCORES!")
        score["THE JOB HUNTERS"] += 1
    else:
      outs += 1
    print("OUTS: ", outs, "\n")
    i += 1
    if i >= 9:
      i = 0
  print(score, "\n")

  print("CHANGE SIDES!\n")
  time.sleep(3)

  outs = 0
  hits = 0
  i = 0
  print("NOW PITCHING: ", str(job_hunters[0].name), " ", str(job_hunters[0].stats), "\n")
  while outs < 3:
    if at_bat_away(i) == "Hit":
      hits += 1
      if hits > 3:
        print("A RUN SCORES!")
        time.sleep(.5)
        score["THE SYSTEM"] += 1
    else:
      outs += 1
      time.sleep(.5)
    print("OUTS: ", outs, "\n")
    i += 1
    if i >= 9:
      i = 0
  return score


    
  # If outs == 3 change sides
  # At bat away function: Simulate one at bat for away team

# At bat home function: Simulates one at bat for home team
def at_bat_home(i):
  out = False
  hit = False
  strikes = 0
  # Loops through Job Hunter list using index.
  print("NOW HITTING: ", str(job_hunters[i].name), " ", str(job_hunters[i].stats))
  while out == False and hit == False: # At bat loop that ends either with an out or a hit
    time.sleep(1)
    if (job_hunters[i].stats["Hitting"] * 5) - (the_system[0].stats["Pitching"] * 3) + random(1, 100) > 85:
      hit = True
      print("HIT")
      time.sleep(.5)
      return "Hit"
    else:
      strikes += 1
      if strikes >= 3:
        out = True
        print("STRIKE 3, YOU'RE OUT!")
        time.sleep(.5)
        return "Out"
      else:
        print("STRIKE", str(strikes) + "!")

def at_bat_away(i):
  out = False
  hit = False
  strikes = 0
  # Loops through Job Hunter list using index.
  print("NOW HITTING: ", str(the_system[i].name), " ", str(job_hunters[0].stats))
  while out == False and hit == False: # At bat loop that ends either with an out or a hit
    time.sleep(1)
    if (the_system[i].stats["Hitting"] * 5) - (job_hunters[0].stats["Pitching"] * 3) + random(1, 100) > 85:
      hit = True
      print("HIT")
      time.sleep(.5)
      return "Hit"
    else:
      strikes += 1
      if strikes >= 3:
        out = True
        print("STRIKE 3, YOU'RE OUT!")
        time.sleep(.5)
        return "Out"
      else:
        print("STRIKE", str(strikes) + "!")
    
play_game()







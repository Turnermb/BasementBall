from random import randrange as random
import time
from teams import generate_team

# Teams
job_hunters = []
the_system = []

# Generates teams using generate_team function found in teams.py
generate_team(job_hunters)
generate_team(the_system)

# Game Logic
score = {"THE JOB HUNTERS": 0, "THE SYSTEM": 0}

def play_game():
  inning = 1
  for i in range(0, 8):
    print("INNING:", inning, "\n")
    play_inning()
    inning += 1

  print("THAT'S THE GAME!")
  print(score)

def play_inning(): # Plays one at bat for both home and away teams.
  outs = 0
  hits = 0
  i = 0

# Home At Bat
  print(score, "\n")
  print("NOW PITCHING: ", str(the_system[0].name), " ", str(the_system[0].stats), "\n")
  while outs < 3:
    time.sleep(1.5)
    if at_bat_home(i) == "Hit":
      hits += 1
      if hits > 3:
        print("A RUN SCORES!")
        score["THE JOB HUNTERS"] += 1
    else:
      outs += 1
    print("OUTS:", outs, "\n")
    i += 1
    if i >= 9:
      i = 0

  # If outs == 3 change sides
  print("CHANGE SIDES!\n")
  time.sleep(3)

  # Away at bat
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
    print("OUTS:", outs, "\n")
    i += 1
    if i >= 9:
      i = 0
  return score

# At bat home function: Simulates one at bat for home team
def at_bat_home(i):
  out = False
  hit = False
  strikes = 0
  # Loops through Job Hunter list and determines a hit or a strike, 3 strikes = 1 out
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

# At bat away: at bat for away team
def at_bat_away(i):
  out = False
  hit = False
  strikes = 0
  print("NOW HITTING: ", str(the_system[i].name), " ", str(job_hunters[0].stats))
  while out == False and hit == False:
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
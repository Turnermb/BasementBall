from random import randrange as random
import time
from teams import generate_team

# Teams
the_system = []
job_hunters = []

# Generates teams using functions found in teams.py
generate_team(the_system)
generate_team(job_hunters)

# Introduces the players on each team.
print("INTRODUCING THE HOME TEAM: THE SYSTEM!\n")
for i in the_system:
    print(i.name.upper())
    time.sleep(.5)

print("\nINTRODUCING THE AWAY TEAM: THE JOB HUNTERS!\n")
for i in job_hunters:
    print(i.name.upper())
    time.sleep(.5)

# Game Logic
toggle = True
home = the_system
away = job_hunters
hitting = ""
pitching = ""
bases = []
home_batter = 0
away_batter = 0
score = { "THE SYSTEM": 0, "THE JOB HUNTERS": 0}

def play_game():
    global score
    inning = 1

    print("\nPLAY BALL!\n")
    for i in range(0, 9):
        print("INNING:", inning, "\n")
        play_inning()
        inning += 1
    if score["THE SYSTEM"] == score["THE JOB HUNTERS"]: # If score is tied at the end of the game, play innings until there's no longer a tie.
        print("EXTRA INNINGS!")
        while score["THE SYSTEM"] == score["THE JOB HUNTERS"]:
            print("INNING:", inning, "\n")
            play_inning()
            inning += 1
    print("THAT'S THE GAME!")
    print(score)
    score["THE SYSTEM"] = 0
    score["THE JOB HUNTERS"] = 0


def play_inning():  # Plays one at bat for both home and away teams.
    global hitting
    global pitching
    global home_batter
    global away_batter
    global bases
    global toggle
    outs = 0

    print(score, "\n")
    for i in range(0, 2):
        if toggle == True: # If toggle = True away team on offense. If False, home team on offense.
            hitting = away
            pitching = home
            i = away_batter # Sets i to the value of the last away batter's index, default 0.    
        elif toggle == False:
            hitting = home
            pitching = away
            i = home_batter # Sets i to the value of the last home batter's index, default 0.

        print("NOW PITCHING:", str(pitching[0].name.upper()), str(pitching[0].stats), "\n")
        while outs < 3: # While outs < 3, if at bat function returns hit advance bases. Otherwise plus one out.
            result = at_bat(i)
            time.sleep(1)
            if result == "Hit":
                bases.insert(0, hitting[i].name) # Inserts name of current batter into bases list.
                manage_runs()
            elif result == "Double":
                bases.insert(0, hitting[i].name)
                for j in range(0,1):
                    bases.insert(0, "empty")
                manage_runs()
            elif result == "Triple":
                bases.insert(0, hitting[i].name)
                for j in range(0,2):
                    bases.insert(0, "empty")
                manage_runs()
            elif result == "Home Run":
                bases.insert(0, hitting[i].name)
                for j in range(0,3):
                    bases.insert(0, "empty")
                manage_runs()
            else:
                outs += 1
            print("OUTS:", outs, "\n")
            i += 1
            if i >= 9: # Returns to the beginning of the batting order after last batter.
                i = 0
        if toggle == True:
            away_batter = i # Stores the last away batter's index in a variable
            print("CHANGE SIDES!\n")
            time.sleep(3)
        else:
            home_batter = i # Stores the last home batter's index in a variable
        bases = [] # Clears bases, outs and current index.
        outs = 0
        i = 0
        toggle = False # Switches toggle to False to change teams. 
    toggle = True # Switches toggle back to True for next inning.

# At bat function: Simulates one at bat for hitting team
def at_bat(i):
    global toggle
    out = False
    hit = False
    strikes = 0
    fielder = 0

    print("NOW HITTING:", str(hitting[i].name.upper()), str(hitting[i].stats))

    while out == False and hit == False:  # At bat loop that ends either with an out or a hit
        if toggle == True:
            i = away_batter
        elif toggle == False:
            i = home_batter
        # Generates offense, defense and pitching deduction numbers.
        offense = (hitting[i].stats["Hitting"] * 3) + random(1, 101)
        defense = (pitching[fielder].stats["Defense"] * 3) + random(1, 101)
        deduction = pitching[0].stats["Pitching"] * 5
        # Offense number minus pitching skill deduction.
        pitch_deducted = (offense - deduction)
        time.sleep(1)
        # If offense number > 75 but is < 75 when pitching is deducted results in a foul ball.
        if offense >= 75 and pitch_deducted < 75: 
            print("FOUL BALL")
            time.sleep(0.5)
            if strikes < 2: # Cannot strike out on foul balls.
                strikes += 1
        elif pitch_deducted > 75:
            fielder = random(0, 9) # Randomly decides which fielder will be selected to defend.
            # If defense > offense a catch is made for an out. Otherwise results in a hit.
            if defense >= offense:
                time.sleep(1)
                print("CAUGHT IN THE OUTFIELD BY", pitching[fielder].name.upper())
                out = True
                time.sleep(0.5)
                return "Out"
            else:
                if (offense == 103 and hitting[i].stats["Hitting"] == 1) or (offense == 106 and hitting[i].stats["Hitting"] == 2) or (offense == 109 and hitting[i].stats["Hitting"] == 3) or (offense == 112 and hitting[i].stats["Hitting"] == 4) or (offense == 115 and hitting[i].stats["Hitting"] == 5): 
                    print("HOME RUN!")
                    time.sleep(0.5)
                    hit = True
                    return "Home Run"
                elif pitch_deducted > 95 and pitch_deducted <= 99:
                    print("DOUBLE!")
                    time.sleep(0.5)
                    hit = True
                    return "Double"
                elif pitch_deducted > 100:
                    print("TRIPLE!")
                    time.sleep(0.5)
                    hit = True
                    return "Triple"
                else:
                    print("HIT")
                    time.sleep(0.5)
                    hit = True
                    return "Hit"
        else:
            strikes += 1
            if strikes >= 3:
                out = True
                print("STRIKE 3, YOU'RE OUT!")
                time.sleep(0.5)
                return "Out"
            else:
                print("STRIKE", str(strikes) + "!")

def manage_runs():
    for i in range(0, len(bases)):
        if len(bases) > 3: # If runner advances home, remove name from end of list.
            if "empty" in bases[-1:]:
                bases.pop()
                continue
            else:
                print("A RUN SCORES!")
                if hitting == away: # Adds one to score of hitting team.
                    score["THE JOB HUNTERS"] += 1
                else:
                    score["THE SYSTEM"] += 1
                bases.pop()
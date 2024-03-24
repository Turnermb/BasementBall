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
home = the_system
away = job_hunters
hitting = ""
pitching = ""
home_batter = 0
away_batter = 0
score = { "THE SYSTEM": 0, "THE JOB HUNTERS": 0}

def play_game():
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


def play_inning():  # Plays one at bat for both home and away teams.
    global hitting
    global pitching
    global home_batter
    global away_batter
    toggle = True
    outs = 0
    hits = 0

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
        while outs < 3: # While outs less than 3 if the result of the at bat was hit, numbers greater than 3 result in a run. Otherwise it's an out.
            time.sleep(1.5)
            if at_bat(i) == "Hit":
                hits += 1
                if hits > 3:
                    print("A RUN SCORES!")
                    if hitting == away: 
                        score["THE JOB HUNTERS"] += 1
                    else:
                        score["THE SYSTEM"] += 1
            else:
                outs += 1
            print("OUTS:", outs, "\n")
            i += 1
            if i >= 9:
                i = 0
        if toggle == True:
            away_batter = i # Stores the last away batter's index in a variable
            print("CHANGE SIDES!\n")
            time.sleep(3)
        elif toggle == False:
            home_batter = i # Stores the last home batter's index in a variable     
        outs = 0
        hits = 0
        i = 0
        toggle = False # Switches toggle to False to change teams. 
    toggle = True # Switches toggle back to True for next inning.

# At bat function: Simulates one at bat for hitting team
def at_bat(i):
    out = False
    hit = False
    strikes = 0
    fielder = 0

    print("NOW HITTING:", str(hitting[i].name.upper()), str(hitting[i].stats))

    while out == False and hit == False:  # At bat loop that ends either with an out or a hit
        # Generates offense and defense numbers.
        offense = (hitting[i].stats["Hitting"] * 5) + random(1, 101)
        defense = (pitching[fielder].stats["Defense"] * 5) + random(1, 101)
        # Offense number minus pitching skill deduction.
        pitch_deducted = (offense - (pitching[0].stats["Pitching"] * 3))
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
            if defense > offense:
                time.sleep(1)
                print("CAUGHT IN THE OUTFIELD BY", pitching[fielder].name.upper())
                out = True
                time.sleep(0.5)
                return "Out"
            else:
                hit = True
                print("HIT")
                time.sleep(0.5)
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

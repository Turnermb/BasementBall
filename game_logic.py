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
    print(i.name)
    time.sleep(.5)

print("\nINTRODUCING THE AWAY TEAM: THE JOB HUNTERS!\n")
for i in job_hunters:
    print(i.name)
    time.sleep(.5)

# Game Logic
home = the_system
away = job_hunters
hitting = ""
pitching = ""
score = { "THE SYSTEM": 0, "THE JOB HUNTERS": 0}

def play_game():
    inning = 1

    print("\nPLAY BALL!\n")
    for i in range(0, 9):
        print("INNING:", inning, "\n")
        play_inning()
        inning += 1

    print("THAT'S THE GAME!")
    print(score)


def play_inning():  # Plays one at bat for both home and away teams.
    global hitting
    global pitching
    toggle = True
    outs = 0
    hits = 0
    i = 0

    print(score, "\n")
    for i in range(0, 2):
        if toggle == True: # If toggle = True away team on offense. If False, home team on offense.
            hitting = away
            pitching = home
        else:
            hitting = home
            pitching = away

        print("NOW PITCHING:", str(pitching[0].name), str(pitching[0].stats), "\n")

        while outs < 3:
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
        outs = 0
        hits = 0
        i = 0
        toggle = False # Switches global toggle to False to change teams.
        
        print("CHANGE SIDES!\n")
        time.sleep(3)
    toggle = True

# At bat function: Simulates one at bat for hitting team
def at_bat(i):
    out = False
    hit = False
    strikes = 0

    print("NOW HITTING:", str(hitting[i].name), str(hitting[i].stats))

    while (out == False and hit == False):  # At bat loop that ends either with an out or a hit
        time.sleep(1)
        if (hitting[i].stats["Hitting"] * 5) - (pitching[0].stats["Pitching"] * 3) + random(1, 100) > 85:
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

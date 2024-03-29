from random import randrange as random, sample
from itertools import combinations
import time
from teams import teams, generate_team
from sys import exit

# Game Logic
toggle = True
iterator = 0
current_field = "Cubicle Park"
home = ""
away = ""
hitting = ""
pitching = ""
bases = []
bases_loaded = False
home_batter = 0
away_batter = 0
outs = 0

# Plays out an entire season of Basement Ball
def play_season():
    # Variables:
    global current_field

    # Gameplay functions:
    def determine_schedule():
        # Each team plays every other team twice at home and twice away.
        com_result = list(combinations(teams, 2))
        result = list(sample(com_result, len(com_result)))

        return result


    # Gameplay logic:
    schedule = determine_schedule()
    schedule_list = list(schedule)
    for i in range(0, len(schedule_list)):
        generate_team(schedule_list[i][0])
        generate_team(schedule_list[i][1])
        current_field = schedule_list[i][0]["Home Field"]
        play_game(schedule_list[i][0], schedule_list[i][1])
        
def play_game(team1, team2):
    # Variables:
    inning = 1

    # Gameplay functions:
    # Determines home field by comparing current field to home field string in dictionary.
    def home_field(team1, team2):
        global home
        global away

        if current_field in team1["Home Field"]:
            home = team1
            away = team2
        elif current_field in team2["Home Field"]:
            home = team2
            away = team1
        else:
            print(team1, team2, current_field)
            exit("NOT VALID TEAMS")

    # Introduces the players on each team.
    def introduce_teams(home, away):
        print("BASEMENT BALL IS COMING TO YOU LIVE FROM:", current_field.upper(), "\n")
        print("INTRODUCING THE HOME TEAM:", home["Name"].upper(),"\n")
        for i in home["Players"]:
            print(i.name.upper())
            time.sleep(.5)

        print("\nINTRODUCING THE AWAY TEAM:", away["Name"].upper(),"\n")
        for i in away["Players"]:
            print(i.name.upper())
            time.sleep(.5)

    # Gameplay logic:
    home_field(team1, team2)
    introduce_teams(home, away)
    print("\nPLAY BALL!\n")
    for i in range(0, 9):
        print("INNING:", inning, "\n")
        play_inning()
        inning += 1
    if home["Score"] == away["Score"]: # If score is tied at the end of the game, play innings until there's no longer a tie.
        print("EXTRA INNINGS!")
        while home["Score"] == away["Score"]:
            print("INNING:", inning, "\n")
            play_inning()
            inning += 1
    print("THAT'S THE GAME!")
    print(home["Name"].upper() + ":",home["Score"], away["Name"].upper() + ":", away["Score"])
    home["Score"] = 0
    away["Score"] = 0


def play_inning():  # Plays one at bat for both home and away teams.
    # Variables:
    global toggle
    global iterator
    global hitting
    global pitching
    global bases_loaded
    global outs

    # Gameplay functions:
    def manage_runs(): # Removes last index of bases until the length of the bases list is 3 or less and counts runs.
        global bases_loaded

        for i in range(0, len(bases)): 
            if len(bases) > 3: 
                if "empty" in bases[-1:]: # Checks to see if last index of bases is a person or string "empty" if string, no run is scored.
                    bases.pop() 
                    continue
                else:
                    print("A RUN SCORES!")
                    if hitting == away: # Adds one to score of hitting team.
                        away["Score"] += 1
                    else:
                        home["Score"] += 1
                    bases.pop()
        if len(bases) == 3 and "empty" not in bases:
            bases_loaded = True
            print("THE BASES ARE LOADED\n")
            time.sleep(0.5)

    def clear_side():
        global iterator
        global home_batter
        global away_batter
        global bases
        global bases_loaded
        global toggle
        global outs

        if toggle == True:
            away_batter = iterator # Stores the last away batter's index in a variable
            print("CHANGE SIDES!\n")
            time.sleep(3)
        else:
            home_batter = iterator # Stores the last home batter's index in a variable
        bases = [] # Clears bases, outs and current index.
        bases_loaded = False
        outs = 0
        iterator = 0
        toggle = False # Switches toggle to False to change teams. 


    # Gameplay logic:
    print(home["Name"].upper() + ":",home["Score"], away["Name"].upper() + ":", away["Score"], "\n")
    for i in range(0, 2):
        if toggle == True: # If toggle = True away team on offense. If False, home team on offense.
            hitting = away
            pitching = home
            iterator = away_batter # Sets i to the value of the last away batter's index, default 0.    
        elif toggle == False:
            hitting = home
            pitching = away
            iterator = home_batter # Sets i to the value of the last home batter's index, default 0.

        print("NOW PITCHING:", str(pitching["Players"][0].name.upper()), str(pitching["Players"][0].stats), "\n")
        while outs < 3: # While outs < 3, if at bat function returns hit advance bases. Otherwise plus one out.
            result = at_bat(iterator)
            time.sleep(1)
            if result == "Hit":
                bases.insert(0, hitting["Players"][iterator].name) # Inserts name of current batter into bases list.
                manage_runs()
            elif result == "Double":
                bases.insert(0, hitting["Players"][iterator].name)
                for j in range(0,1): # Advances player at bat to second base and fills first base with string "empty".
                    bases.insert(0, "empty")
                manage_runs()
            elif result == "Triple":
                bases.insert(0, hitting["Players"][iterator].name)
                for j in range(0,2): # Advances player at bat to third base and fills first and second base with string "empty".
                    bases.insert(0, "empty")
                manage_runs()
            elif result == "Home Run":
                bases.insert(0, hitting["Players"][iterator].name)
                for j in range(0,3): # Advances player at bat home and fills all bases with string "empty".
                    bases.insert(0, "empty")
                manage_runs()
            else:
                outs += 1
            print("OUTS:", outs, "\n")
            iterator += 1
            if iterator >= 9: # Returns to the beginning of the batting order after last batter.
                iterator = 0
        clear_side() # Clears variables and switches toggle to false to change batting team to home team.
    toggle = True # Returns toggle to true to change batting team back to away team before next inning.



# At bat function: Simulates one at bat for hitting team
def at_bat(i):
    # Variables:
    global toggle
    global bases_loaded
    out = False
    hit = False
    strikes = 0
    fielder = 0

    # Gameplay functions:

    # Gameplay logic:
    print("NOW HITTING:", str(hitting["Players"][i].name.upper()), str(hitting["Players"][i].stats))

    while out == False and hit == False:  # At bat loop that ends either with an out or a hit
        if toggle == True:
            i = away_batter
        elif toggle == False:
            i = home_batter
        # Generates offense, defense and pitching deduction numbers.
        offense = (hitting["Players"][i].stats["Hitting"] * 3) + random(1, 101)
        max_hit = (hitting["Players"][i].stats["Hitting"] * 3) + 100
        defense = (pitching["Players"][fielder].stats["Defense"] * 3) + random(1, 101)
        deduction = pitching["Players"][0].stats["Pitching"] * 3
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
                print("CAUGHT IN THE OUTFIELD BY", pitching["Players"][fielder].name.upper() + "\n")
                out = True
                time.sleep(0.5)
                return "Out"
            else:
                # Takes current value of offense/pitch_deducted and compares against threshold to determine number of bases advanced.
                # If player rolls the max value for their hitting stat before pitcher deduction a home run is scored.
                if offense == max_hit:
                    if bases_loaded == True:
                        print("~~~~~ IT'S A GRAND SLAM! ~~~~~\n")
                        bases_loaded = False
                    else:
                        print("HOME RUN!\n")
                    time.sleep(0.5)
                    hit = True
                    return "Home Run"
                elif pitch_deducted > 95 and pitch_deducted <= 99:
                    print("DOUBLE!\n")
                    time.sleep(0.5)
                    hit = True
                    return "Double"
                elif pitch_deducted > 100:
                    print("TRIPLE!\n")
                    time.sleep(0.5)
                    hit = True
                    return "Triple"
                else:
                    print("HIT\n")
                    time.sleep(0.5)
                    hit = True
                    return "Hit"
        else:
            strikes += 1
            if strikes >= 3:
                out = True
                print("STRIKE 3, YOU'RE OUT!\n")
                time.sleep(0.5)
                return "Out"
            else:
                print("STRIKE", str(strikes) + "!")

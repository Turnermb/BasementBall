# Basement Ball

'''
TO DO:
Move game logic into module and get game working
Refactor at bats into one function using top(away) and bottom(home) of inning.
Extra innings in case of tie
Player classes/stats

Stretch goals:
Add more teams
Season/Post Season
Website? 
Data API
'''

# Imports
from teams import generate_team
from game_logic import play_game

# Teams
job_hunters = []
the_system = []

# Generates teams using function found in teams.py
generate_team(job_hunters)
generate_team(the_system)

# Plays full game using functions found in game_logic.py
play_game()







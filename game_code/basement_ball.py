# Basement Ball
'''
Dependencies:
    Requests,
    Django
'''



# Imports
from game_logic import play_game
from teams import teams

# Plays full game using functions found in game_logic.py
play_game(teams[0], teams[1])







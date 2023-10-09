from steam import Steam
import json
from decouple import config

KEY = config("STEAM_API_KEY")

steam = Steam(KEY)

def search_game(search_request : str):
    response = steam.apps.search_games(search_request)
    
    return response
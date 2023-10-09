from steam import Steam
import json
from decouple import config

KEY = config("STEAM_API_KEY")

steam = Steam(KEY)

def get_steamid(username :str) -> int:
    response = steam.users.get_steamid(username)
    
    return response

def get_bot_steamid():
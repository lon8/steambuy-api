from steam import Steam
import json
from decouple import config

def get_steamid(username :str, bot_id : int) -> int:
    
    KEY = config(f"BOT{bot_id}_KEY")
    
    steam = Steam(KEY)
    
    response = steam.users.get_steamid(username)
    
    return response
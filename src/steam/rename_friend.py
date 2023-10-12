import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config
from db.tables.models import Bot

DB_URL = config('DATABASE_URL')

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

def get_bot_steamid_by_id(bot_id) -> str | None:
    session = SessionLocal()
    bot = session.query(Bot).filter(Bot.id == bot_id).first()
    session.close()
    return bot.steam_id if bot else None

def get_bot_steamapi_by_id(bot_id) -> str | None:
    session = SessionLocal()
    bot = session.query(Bot).filter(Bot.id == bot_id).first()
    session.close()
    return bot.steam_api_key if bot else None

def change_friend_nickname(steam_api_key, friend_steam_id, new_nickname) -> None:
    url = f"https://api.steampowered.com/ISteamUser/SetPlayerNickname/v1/?key={steam_api_key}"
    data = {
        "steamid": friend_steam_id,
        "newname": new_nickname
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f"Никнейм друга успешно изменен на {new_nickname}")
    else:
        print(f"Ошибка при изменении никнейма: {response.status_code}")
        
        
# Как будет выглядеть функция для изменения никнейма
def kernel_friends(bot_id, ):
    return #
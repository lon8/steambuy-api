from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from db.tables.models import User, Bot
from decouple import config

DB_URL = config("DATABASE_URL")

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()


# Users Table

def create_user(user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Проверка пользователя в базе данных
def get_user_by_email(email: str):
    return db.query(User).filter(User.email == email).first()


# Bots Table

def get_bot_steamid(bot_id : int) -> int | None:
    session = SessionLocal()
    bot = session.query(Bot).filter(Bot.id == bot_id).first()
    session.close()
    return bot.steam_id if bot else None
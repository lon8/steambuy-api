from sqlalchemy import Column, Integer, String, DateTime, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from decouple import config

DB_URL = config("DATABASE_URL")

Base = declarative_base()

engine = create_engine(DB_URL, connect_args={})

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, unique=True, nullable=False)
    email = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    steam_id = Column(String(32))  # Мы добавим его позже
    nickname = Column(String(32), nullable=False)
    sesid = Column(Integer, nullable=False)
    registration_date = Column(DateTime, default=datetime.now)

class Bot(Base):
    __tablename__ = 'bots'

    id = Column(Integer, primary_key=True)
    steam_id = Column(String(32), unique=True, nullable=False)
    steam_api_key = Column(String(64), unique=True)
    balance = Column(Integer, default=10000)

class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    opcode = Column(String(64), nullable=False)
    opcost = Column(Integer)
    
    
Base.metadata.create_all(bind=engine)

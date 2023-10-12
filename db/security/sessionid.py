import secrets
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

from db.tables.models import Session

DB_URL = config('DATABASE_URL')

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

def generate_sid() -> str:
    return secrets.token_hex(32)

def get_sid(user_id) -> str | None:
    session = SessionLocal()
    sid = session.query(Session).filter(Session.user_id == user_id).first()
    session.close()
    return sid
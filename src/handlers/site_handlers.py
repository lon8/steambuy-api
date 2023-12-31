# Engine imports
from datetime import datetime
from fastapi import APIRouter, HTTPException
import secrets

# Data imports
from db.tables.forms import UserLoginForm, UserRegisterForm
from db.tables.funcs import create_user, get_user_by_email, create_session
from db.security.hash import Hashing
from db.security.uidcreate import generate_seven_digit_id
from db.tables.models import User, Session
from db.tables.funcs import db
from db.security.sessionid import get_sid, generate_sid
from src.steam.searching_game import search_game


srouter = APIRouter()

@srouter.get('/api/site/')
def start():
    return HTTPException(204, 'No Content')

@srouter.post('/api/site/reg/')
def register(register_form : UserRegisterForm):
    if db.query(User).filter(User.email == register_form.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # Создаем пользователя и хэшируем пароль
    user = User(uid=generate_seven_digit_id(), email=register_form.email, password=Hashing().get_password_hash(register_form.password),
                nickname=register_form.nickname, registration_date=str(datetime.now()))

    # Сохраняем пользователя в базе данных
    db_user = create_user(user)

    # C сессией то же самое 
    session = Session(sid=generate_sid(), user_id=user.id)
    
    db_session = create_session(session=session)

    
    # Закрываем соединение с базой данных
    db.close()

    return {"status": 200, "msg": "User registered successfully"}

@srouter.post('/api/site/login/')
def login(login_form : UserLoginForm):
    user = get_user_by_email(login_form.email)

    if user is None or not Hashing().verify_password(login_form.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    return {
        'status': 200,
        'msg': 'Login Succesful',
        'session_id': get_sid(user.uid)
    }

@srouter.post('/api/site/getgame/')
def get_game(payload : dict):
    try:
        return search_game(payload['query'])
    except KeyError:
        raise HTTPException(400, detail='KeyError. Please try this response with other key in payload')
    

from fastapi import APIRouter


brouter = APIRouter()

@brouter.get('/api/bot/')
def start():
    return "Hello for bot's"
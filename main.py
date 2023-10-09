from fastapi import FastAPI
from src.handlers.site_handlers import srouter
from src.handlers.bot_handlers import brouter



def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(srouter)
    application.include_router(brouter)
    
    return application

app = get_application()
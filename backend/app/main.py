from fastapi import FastAPI

from backend.app.routes import users, chanels, movies, advertisements
from backend.app.config.db import init_db
from contextlib import asynccontextmanager
from .models.movie import Movie
from .models.chanels import Chanel


@asynccontextmanager
async def lifespan(app:FastAPI):
    init_db()
    yield
    
    
    
app = FastAPI(lifespan=lifespan)

app.include_router(users.router, tags=['/User'] )
app.include_router(movies.router,tags=['/Movies'] )
app.include_router(chanels.router,tags=['/chanels'] )
app.include_router(advertisements.router, tags=['/advertisements'])


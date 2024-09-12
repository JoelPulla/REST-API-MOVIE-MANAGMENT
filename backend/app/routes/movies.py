from fastapi import APIRouter

from sqlmodel import select
from sqlalchemy import func
from ..config.db import Session, engine
from ..models.movie import Movie, Category
from ..schemas.movie_category_schema import MovieCreate, MoviePublic, CategoryCreate, CategoryPublic



router = APIRouter()


@router.post('/movies', response_model=MoviePublic)
def create_movie(movie: MovieCreate):
    with Session(engine) as session:
        db_movie = Movie.model_validate(movie)
        session.add(db_movie)
        session.commit()
        session.refresh(db_movie)
        return db_movie
    
    
############### Categories Movies ##############

@router.post('/categories', )
def create_category(category: CategoryCreate):

    with Session(engine) as session:
        
        query = session.exec(select(Category).where(Category.name == category.name)).first()
        
        if query:   
            return 'ya existe una categoria '
        
        new_category = Category.model_validate(category)
        session.add(new_category)
        session.commit()
        session.refresh(new_category)
        return new_category
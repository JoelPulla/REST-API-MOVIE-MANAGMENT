from fastapi import APIRouter,Depends, HTTPException

from sqlmodel import select
from sqlalchemy import func
from ..config.db import Session, engine
from ..models.movie import Movie, Category, MovieCategory
from ..schemas.movie_category_schema import MovieCreate, MoviePublic, MoviePublicWhitCategory,CategoryCreate, CategoryPublic, CategoryPublicWithMovies
from ..schemas.responses import Message


router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session



# verificar funcionamineto
@router.get('/movies/{id}', response_model=MoviePublicWhitCategory)
def read_movies(*, sesscion: Session =Depends(get_session), id:int):
    
    query = sesscion.get(Movie, id)
    if not query:
        raise HTTPException(status_code=404, detail= 'not hero by id')
    
    return query



@router.post('/movies', response_model=MovieCreate)
def create_movie(*, session:Session = Depends(get_session), movie: MovieCreate):
    
    # query = session.exec(select(Movie).where(func.lower(Movie.movie_title) == func.lower(movie.movie_title))).first()
    
    # if query:
    #     raise HTTPException(status_code=409, detail= 'Movie alredy exist')
    
    
    new_movie = Movie(movie_title=movie.movie_title,
        overview=movie.overview,
        id_tmdb=movie.id_tmdb,
        url_video=movie.url_video,
        is_youtube=movie.is_youtube,
        poster_path=movie.poster_path,
        background_path=movie.background_path,
        voute_range=movie.voute_range,
        popularity=movie.popularity,
        created_at=movie.created_at,
        release=movie.release)
    
    session.add(new_movie)
    session.commit()
    session.refresh(new_movie)
    
     # Relacionar la película con las categorías usando la tabla pivote
    for category_id in movie.category_ids:
        # Verificar que la categoría exista
        category = session.exec(select(Category).where(Category.id == category_id)).first()
        if category:
            # Crear la relación en la tabla pivote MovieCategory
            movie_category = MovieCategory(movie_id=new_movie.id, category_id=category.id)
            session.add(movie_category)
        else:
            raise ValueError(f"Category with ID {category_id} not found")
    
    
    # db_movie = Movie.model_validate(movie)  
    # session.add(db_movie)
    # session.commit()
    # session.refresh(db_movie)
    # return db_movie
    
    session.commit()
    
    # Refrescar la película para obtener las relaciones actualizadas
    session.refresh(new_movie)

    # Devolver la película con las categorías relacionadas
    return new_movie
    

############### Categories Movies ##############

@router.post('/categories',response_model=CategoryPublic )
def create_category(*, session: Session = Depends(get_session), category: CategoryCreate):
    
    query = session.exec(select(Category).where( func.lower(Category.name)== func.lower(category.name))).first()
    
    if query:   
        raise HTTPException(status_code=409, detail='category already exists')
    
    new_category = Category.model_validate(category)
    session.add(new_category) 
    session.commit()
    session.refresh(new_category)
    return new_category

@router.get('/categories/{id}', response_model=CategoryPublicWithMovies)
def read_cateorie_by_id(*, session : Session= Depends(get_session), id:int ):
    query =  session.get(Category, id)
    if not query:
        raise HTTPException (status_code=404, detail='no exist dat by {id}'.format(id = id))
    return query


@router.get('/categories', response_model=list[CategoryPublic])
def read_categories(*, session: Session = Depends(get_session)):
  
    categories = session.exec(select(Category)).all()
    return categories


@router.delete('/categories/{id}', response_model= Message)
def delete_category(*,session: Session = Depends(get_session), id: int ):
    
    category  = session.exec(select(Category).where(Category.id == id)).first()
    
    if not category:
        raise HTTPException(status_code=404, detail='Category not found')
    
    session.delete(category)
    session.commit()
    return Message(message='Category delete successfully')



from sqlmodel import Field, SQLModel
from datetime import date


""" Movie"""
class Movie(SQLModel, table= True):
    
    id: int | None = Field(default=None, primary_key=True)
    movie_title :str
    overview :str
    id_tmdb : int
    url_video: str
    is_youtube: bool
    poster_path: str 
    background_path : str
    voute_range : float 
    popularity :float
    created_at : date
    release: date
    
    # #relacion con Category
    # categories = relationship("CategoryModel", secondary= "movie_category", back_populates="movies" )
    
"""Movie_Category table pivote """



""" Category """
class Category(SQLModel, table= True):
    
    id: int | None = Field(primary_key=True, default=None,)
    name: str
    is_active: bool
    created_at: date
    posther_path: str
    
    
    
    # # Relacion con Categorias
    # movies =  relationship("MovieModel", secondary= "movie_category",  back_populates="categories")
    

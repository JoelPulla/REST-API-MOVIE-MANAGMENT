from sqlmodel import Field, SQLModel, Relationship
from datetime import date

"""Movie_Category table pivote """
class MovieCategory(SQLModel, table= True):
    category_id : int |  None = Field(default=None, foreign_key="", primary_key=True)  
    movie_id: int | None = Field(default=None, foreign_key="", primary_key=True)
    

""" Category """
class Category(SQLModel, table= True):
    
    id: int | None = Field(primary_key=True, default=None,)
    name: str
    is_active: bool
    created_at: date
    posther_path: str
    
    movies: list["Movie"] = Relationship(back_populates="movies", link_model=MovieCategory)
     

"""Movie"""
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
    
    categories: list[Category]= Relationship(back_populates="categories", link_model=MovieCategory)

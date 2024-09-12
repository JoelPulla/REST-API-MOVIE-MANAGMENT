from sqlmodel import Field, SQLModel, Relationship
from datetime import date
from ..schemas.movie_category_schema import MovieBase, categoryBase

"""Movie_Category table pivote """
class MovieCategory(SQLModel, table= True):
    category_id : int |  None = Field(default=None, foreign_key="category.id", primary_key=True)  
    movie_id: int | None = Field(default=None, foreign_key="movie.id", primary_key=True)
    

""" Category """
class Category(categoryBase, table= True):
    
    id: int | None = Field(primary_key=True, default=None,)
    #many to many
    movies: list["Movie"] = Relationship(back_populates="categories", link_model=MovieCategory)
     

"""Movie"""
class Movie(MovieBase, table= True):
    
    id: int | None = Field(default=None, primary_key=True)
    #many to many 
    categories: list[Category]= Relationship(back_populates="movies", link_model=MovieCategory)

from sqlmodel import SQLModel
from datetime import date


class MovieBase(SQLModel): 
    movie_title :str
    overview :str
    id_tmdb : int |None = None
    url_video: str
    is_youtube: bool
    poster_path: str 
    background_path : str
    voute_range : float 
    popularity :float
    created_at : date
    release: date



class MovieCreate(MovieBase):
    pass
 
 
    
class MoviePublic(MovieBase):
    id:int

    

####################### Category #######################
class categoryBase(SQLModel):
    name: str
    is_active: bool
    created_at: date
    posther_path: str


class CategoryCreate(categoryBase):
    pass
    
class CategoryPublic(categoryBase):
    id: int
    

    
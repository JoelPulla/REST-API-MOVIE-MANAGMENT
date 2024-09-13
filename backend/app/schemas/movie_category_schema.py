from sqlmodel import SQLModel, Field
from datetime import date


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
    

    
####################### Movie #######################
    
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
    
    category_id: int |None = Field(default=None, foreign_key="category.id")



class MovieCreate(MovieBase):
    category_ids:list[int]
 
 
class MoviePublic(MovieBase):
    id:int

####################### relations Schemas #######################

#revisar para ver si debo cambiar para poder hacer una consulta a la movi con la lista de categorias 
class MoviePublicWhitCategory(MoviePublic):
    category: list[CategoryPublic]= []
    
    
class CategoryPublicWithMovies(CategoryPublic):
    movies: list[MoviePublic] = []

    
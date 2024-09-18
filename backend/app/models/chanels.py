from sqlmodel import SQLModel, Field, Relationship
from ..schemas.chanels import ChanelBase, CategoryTvBase

class CategoryTv(CategoryTvBase, table = True): 
    id :int = Field(default=None, primary_key=True) 

    chanels: list["Chanel"] = Relationship(back_populates="chanel")





class Chanel(ChanelBase, table = True):
    
    id: int = Field(default=None, primary_key=True) 
    
    category_id: int|None= Field(default=None, foreign_key="categorytv.id")
    category: CategoryTv| None = Relationship(back_populates="chanels")
    
    
    
    
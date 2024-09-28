from sqlmodel import Field, Relationship
from ..schemas.chanels import ChanelBase, CategoryTvBase
from typing import Optional


class CategoryTv(CategoryTvBase, table = True): 
    id :int = Field(default=None, primary_key=True) 
    
    chanels: list["Chanel"] = Relationship(back_populates="categorytv")


 
class Chanel(ChanelBase, table = True):
    id: int = Field(default=None, primary_key=True) 

    categorytv: CategoryTv|None  = Relationship(back_populates= "chanels")
    
    
    
    
    
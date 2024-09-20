from sqlmodel import SQLModel, Field
from datetime import date


    
########## CategoryTv #######

class CategoryTvBase(SQLModel):
    name: str 
    is_active: bool
    posther_path: str 
    created_at: date
    
class CategooryTvCreate(CategoryTvBase):
    pass

class CategoryTvPublic(CategoryTvBase):
    id: int 
    
class CategoryTvUpdate(SQLModel):
    name: str 
    is_active: bool
    posther_path: str 
    created_at: date
    

########## Chanel #######

class ChanelBase(SQLModel):
    name: str 
    overview: str | None = None
    url: str 
    is_active:bool
    is_youtube : bool
    created_at: date
    update_at:date
    
    
    
class ChanelCreate(ChanelBase):
    pass

class ChanelPublic(ChanelBase):
    id: int
    
class ChanelUpdate(SQLModel):
    name: str 
    overview: str | None = None
    url: str 
    is_active:bool
    is_youtube : bool
    created_at: date
    update_at:date
    

# class ChanelPublicWhitCategoryTv(ChanelPublic):
#     category: CategoryTvPublic | None = None
    
# class CategoryTvWhitChanels(CategoryTvPublic):
#     chanels: list[ChanelPublic]= []
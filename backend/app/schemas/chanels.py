from sqlmodel import SQLModel, Field
from datetime import date


class ChanelBase(SQLModel):
    
    name: str 
    overview: str | None = None
    url: str 
    is_active:bool
    is_youtube : bool
    created_at: date
    update_at:date
    
    category_id: int | None = Field(default=None, foreign_key="category.id")
    
class CreateChanel(ChanelBase):
    pass
    
########## CategoryTv #######

class CategoryTvBase(SQLModel):
    
    name: str 
    is_active: bool
    posther_path: str 
    created_at: date
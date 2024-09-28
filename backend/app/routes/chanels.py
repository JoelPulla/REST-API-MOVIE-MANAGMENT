from fastapi import APIRouter, Depends, HTTPException

from sqlmodel import select, func
from ..schemas.chanels import *
from ..config.db import Session, engine
from ..models.chanels import *


router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session


@router.post('/chanel', response_model=ChanelPublic)
def create_chanel(*, session: Session = Depends(get_session), chanel: ChanelCreate):
    
    db_chanel = Chanel.model_validate(chanel)
    session.add(db_chanel)
    session.commit()
    session.refresh(db_chanel)
    
    return db_chanel    


@router.delete('/chanel/{id}')
def delete_chanel(*, session: Session = Depends(get_session), id: int):
    
    query = session.get(Chanel, id)
    if not query:
        raise HTTPException(status_code=404, detail=f'not found {id}') 
    
    session.delete(query)
    session.commit()
    
    return {"ok": True}

################### Category Tv ######################

@router.post('/CategoryTv', response_model=CategoryTvPublic)
def create_categorytv(*, session: Session= Depends(get_session), categrytv: CategooryTvCreate):
    
    db_category = session.exec(select(CategoryTv).where(func.lower(CategoryTv.name) == func.lower(categrytv.name))).first()

    if db_category:
        raise HTTPException (status_code=409, detail='category alredy exist')
    
    db_category = CategoryTv.model_validate(categrytv)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)

    return db_category


@router.get('/Categories    ', response_model=list[CategoryTvPublic])
def read_all_categories(*, session: Session = Depends(get_session)):
    query = session.exec(select(CategoryTv)).all()
    return query

@router.delete('/Category/{id}')
def delete_category(*, session: Session = Depends(get_session), id:int):
    query = session.get(CategoryTv, id)
    session.delete(query)
    session.commit
    return {'ok':True}


@router.get('/Category/Chanels/{id}', response_model=CategoryTvWhitChanels)
def read_cateoryWhitChanel(*, session : Session= Depends(get_session), id:int):
    query = session.get(CategoryTv, id)
    
    if not query:
        raise HTTPException(status_code=404, detail="No data" )
    
    return query

@router.get('/Categories/Chanels', response_model= list[CategoryTvWhitChanels] )
def read_all_categories_Whit_chanels(*, session:Session = Depends(get_session)):
    
    query = session.exec(select(CategoryTv))
    
    if not query:
        raise HTTPException (status_code=404, detail="No data")
    
    return query
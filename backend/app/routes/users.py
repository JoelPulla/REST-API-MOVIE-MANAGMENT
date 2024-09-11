from fastapi import APIRouter

router = APIRouter()

@router.get('/user')
def movies():
    return 'User'
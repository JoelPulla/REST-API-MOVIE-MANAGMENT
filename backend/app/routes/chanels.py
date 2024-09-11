from fastapi import APIRouter

router = APIRouter()

@router.get('/chanels')
def movies():
    return 'User'
from fastapi import APIRouter

router = APIRouter()

@router.get('/movies')
def movies():
    return 'movies'
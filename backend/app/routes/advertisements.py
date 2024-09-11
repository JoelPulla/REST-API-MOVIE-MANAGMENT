from fastapi import APIRouter

router = APIRouter()

@router.get('/advertisements')
def movies():
    return 'advertisement'
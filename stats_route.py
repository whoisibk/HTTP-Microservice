from fastapi import APIRouter
from metrics import metrics

router = APIRouter()


@router.get("/stats")
def stats():
    return metrics

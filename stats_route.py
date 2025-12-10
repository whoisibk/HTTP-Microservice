from fastapi import APIRouter

router = APIRouter()


@router.get("/stats")
def stats():
    from metrics import metrics
    return metrics

from fastapi import APIRouter

router = APIRouter()


@router.get("/stats")
def stats():
    from user_tokenBucket import metrics
    return metrics

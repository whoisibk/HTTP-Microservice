from fastapi import FastAPI, HTTPException, Request
from stats_route import router as stats_router
from user_tokenBucket import metric

api = FastAPI()


@api.get("/test1", response_model=dict)
def test1(request: Request):

    client_host = request.client.host
    buckets = metric(client_host=client_host)

    for bucket in buckets:
        if bucket == client_host:
            client_host["total_requests"] += 1

            if client_host["curr_tokens"] < 1:
                client_host["rate_limited_requests"] += 1
                return {"Too many requests"}

            client_host["curr_tokens"] -= 1
            return {"This is the first test!"}


api.include_router(stats_router)

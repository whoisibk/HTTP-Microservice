from fastapi import FastAPI, HTTPException, Request
from stats_route import router as stats_router
from user_tokenBucket import metric

api = FastAPI()


@api.get("/test1", response_model=dict)
def test1(request: Request):

    client_host = request.client.host
    buckets: dict = metric(client_host=client_host)

    for ip in buckets:
        if ip == client_host:
            user = buckets[ip]

            user["total_requests"] += 1

            if user["curr_tokens"] < 1:
                user["rate_limited_requests"] += 1
                return {"message": "Too many requests"}

            user["curr_tokens"] -= 1
            return {
                "IP Address": client_host,
                "Number of Requests": user["total_requests"],
                "No. of Tokens Available": user["curr_tokens"],
                "Timestamp": user["last_refill_time"].strftime("%H:%M:%S"),
                "Status_Code": 200,
            }


# api.include_router(stats_router)

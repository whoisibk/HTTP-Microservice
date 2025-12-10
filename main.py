from fastapi import FastAPI, HTTPException, Request
from stats_route import router as stats_router

api = FastAPI()


total_requests, test1_requests, test2_requests, test3_requests = 0, 0, 0, 0


@api.get("/test1", response_model=dict)
def test1(request: Request):
    global total_requests, test1_requests

    client_host = request.client.host
    total_requests += 1
    test1_requests += 1
    return {"This is the first test!"}


@api.get("/test2", response_model=dict)
def test2(request: Request):
    global total_requests, test2_requests

    client = request.client.host
    total_requests += 1
    test2_requests += 1
    return {"This is the second test!"}


@api.get("/test3", response_model=dict)
def test3(request: Request):
    global total_requests, test3_requests

    client = request.client.host
    total_requests += 1
    test3_requests += 1
    return {"This is the third test!"}


api.include_router(stats_router)

from fastapi import FastAPI
from stats_route import router as stats_router

api = FastAPI()


total_requests, test1_requests, test2_requests, test3_requests = 0, 0, 0, 0


@api.get("/test1")
def test1():
    global total_requests, test1_requests

    total_requests += 1
    test1_requests += 1
    return {"This is the first test!"}


@api.get("/test2")
def test2():
    global total_requests, test2_requests

    total_requests += 1
    test2_requests += 1
    return {"This is the second test!"}


@api.get("test3")
def test3():
    global total_requests, test3_requests

    total_requests += 1
    test3_requests += 1
    return {"This is the third test!"}

api.include_router(stats_router)
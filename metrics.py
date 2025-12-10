from time import time
from datetime import datetime
from main import (
    total_requests,
    test1_requests,
    test2_requests,
    test3_requests,
    client_host,
)

max_tokens = 5
token_refill_rate = 1  # tokens per second


metrics = {
    "Total Requests Made": total_requests,
    "Test 1 Requests": test1_requests,
    "Test 2 Requests": test2_requests,
    "Test 3 Requests": test3_requests,
}

current_time = time()

buckets = {

    }

if client_host not in buckets:
    buckets[client_host] = {
        # "Total Requests Made": total_requests,
        # "Test 1 Requests": test1_requests,
        # "Test 2 Requests": test2_requests,
        # "Test 3 Requests": test3_requests,
        "tokens": 1,
        "last_refill_time": datetime.strptime(time())

    }

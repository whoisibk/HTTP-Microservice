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


# # metrics = {
#     "Total Requests Made": total_requests,
#     "Test 1 Requests": test1_requests,
#     "Test 2 Requests": test2_requests,
#     "Test 3 Requests": test3_requests,
# }


buckets = {}

if client_host not in buckets:
    buckets[client_host] = {
        # "Total Requests Made": total_requests,
        # "Test 1 Requests": test1_requests,
        # "Test 2 Requests": test2_requests,
        # "Test 3 Requests": test3_requests,
        "tokens": 5,
        "last_refill_time": datetime.strptime(
            str(datetime.now().time())[:-7], "%H:%M:%S"
        ),
    }
else:
    for bucket in buckets:
        if bucket == client_host:
            current_time: datetime = datetime.strptime(
                str(datetime.now().time())[:-7], "%H:%M:%S"
            )
            elapsed_seconds = (
                current_time - datetime(client_host["last_refill_time"])
            ).total_seconds()
            tokens_to_add: int = int(elapsed_seconds) * token_refill_rate
            client_host["tokens"] += tokens_to_add

            if client_host["tokens"] > max_tokens:
                client_host["tokens"] = max_tokens
                client_host["last_refill_time"] = datetime.strptime(
                    str(datetime.now().time())[:-7], "%H:%M:%S"
                )

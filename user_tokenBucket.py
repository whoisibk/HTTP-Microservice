from datetime import datetime

buckets = {}

def metric(client_host: str):
    max_tokens = 5
    token_refill_rate = 1  # tokens per second


    if client_host not in buckets:
        buckets[client_host] = {
            "curr_tokens": 5,
            "last_refill_time": datetime.strptime(
                str(datetime.now().time())[:-7], "%H:%M:%S"
            ),
            "rate_limited_requests": 0,
            "total_requests": 0,
        }
    else:
        for ip in buckets:
            if ip == client_host:
                user = buckets[ip]
                current_time: datetime = datetime.strptime(
                    str(datetime.now().time())[:-7], "%H:%M:%S"
                )

                elapsed_seconds: float = (
                    current_time - user["last_refill_time"]
                ).total_seconds()

                tokens_to_add: int = int(elapsed_seconds) * token_refill_rate
                user["curr_tokens"] += tokens_to_add

                if user["curr_tokens"] > max_tokens:
                    user["curr_tokens"] = max_tokens
                    user["last_refill_time"] = datetime.strptime(
                        str(datetime.now().time())[:-7], "%H:%M:%S"
                    )

    return buckets


if __name__ == "__main__":
    metric()

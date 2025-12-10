from datetime import datetime


def metric(client_host: str):
    max_tokens = 5
    token_refill_rate = 1  # tokens per second

    buckets = {}

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
        for bucket in buckets:
            if bucket == client_host:
                current_time: datetime = datetime.strptime(
                    str(datetime.now().time())[:-7], "%H:%M:%S"
                )

                elapsed_seconds: float = (
                    current_time - datetime(client_host["last_refill_time"])
                ).total_seconds()

                tokens_to_add: int = int(elapsed_seconds) * token_refill_rate
                client_host["tokens"] += tokens_to_add

                if client_host["tokens"] > max_tokens:
                    client_host["tokens"] = max_tokens
                    client_host["last_refill_time"] = datetime.strptime(
                        str(datetime.now().time())[:-7], "%H:%M:%S"
                    )

    return buckets


if __name__ == "__main__":
    metric()

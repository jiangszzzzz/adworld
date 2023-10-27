## WRB Training-WWW-Robots


---

In this little training challenge, you are going to learn about the Robots_exclusion_standard.
The robots.txt file is used by web crawlers to check if they are allowed to crawl and index your website or only parts of it.
Sometimes these files reveal the directory structure instead protecting the content from being crawled.

Enjoy!

---

可直接访问
http://61.147.171.105:51688/robots.txt

得到：

User-agent: *
Disallow: <font color=yellow>/fl0g.php（暴露了文件结构）</font>



User-agent: Yandex
Disallow: *

访问

http://61.147.171.105:51688/fl0g.php

### flag

cyberpeace{f1dea06c5add0c6d285d32dc7859168d}

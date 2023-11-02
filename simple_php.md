## simple_php

---

```
<?php
show_source(__FILE__);
include("config.php");
$a=@$_GET['a'];
$b=@$_GET['b'];
if($a==0 and $a){
    echo $flag1;
}
if(is_numeric($b)){
    exit();
}
if($b>1234){
    echo $flag2;
}
?>
```

* 代码审计，php == 为若类型比较
* 跳过 is_numeric($b)
* '>' 为弱类型比较 


flag1 flag2 拼接后为flag

---

### payload
/?a=0a&b=12345a

Cyberpeace{647E37C7627CC3E4019EC69324F66C7C}
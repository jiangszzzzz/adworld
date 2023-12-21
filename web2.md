## web2
题目
* 先时将flag字符串逆序
* 然后每一个ascii码数值+1
* 然后base64加密
* 然后逆序
* 然后再rot13加密

---

### 反向分析
```
<?php
$miwen="a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws";
echo $miwen;
echo'</br>';

// 题目给的加密函数
function encode($str){
    $_o=strrev($str);
    // echo $_o;
        
    for($_0=0;$_0<strlen($_o);$_0++){
       
        $_c=substr($_o,$_0,1);
        $__=ord($_c)+1;
        $_c=chr($__);
        $_=$_.$_c;   
    } 
    return str_rot13(strrev(base64_encode($_)));
}

// 解密函数
function decode($str){
	$str1 = base64_decode(strrev(str_rot13($str)));
    echo $str1;
    echo'</br>';

    for($_0=0;$_0<strlen($str1);$_0++){

        $_c=substr($str1,$_0,1);
        $__=ord($_c)-1;
        $_c=chr($__);
        $_=$_.$_c;   
    }

    return strrev($_);
}

echo decode($miwen);
?>
```
### flag
flag:{NSCTF_b73d5adfb819c64603d7237fa0d52977}
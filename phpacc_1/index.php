<!--
PHP Account Creator v 1.3
for use with the Sphere Ultima Online emulator version 55i

(c) 2003 Ron Custer

-->
<HTML>
<HEAD>
</HEAD>
<BODY>

<?php

$token = array("a","b","c","d","e","f","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9");
$password= $token[rand(0, 35)] . $token[rand(0, 35)] . $token[rand(0, 35)] . $token[rand(0, 35)] . $token[rand(0, 35)] . $token[rand(0, 35)]; // generate password
$emails = array("root@127.0.0.1");

require "config.php";

// Start security patch
if (ini_get('register_globals')){
ini_set("register_globals",0);
}

if ((isset($_GET['username']))||(isset($_GET['email']))||(isset($_GET['password']))){
   if ($keeplog){
	$time = date("Y/m/d H:i:s");
	if (getenv('HTTP_X_FORWARDED_FOR')) { 
  		$ip = getenv('HTTP_X_FORWARD_FOR'); 
		$host = gethostbyaddr($ip); 
	} else { 
		$ip = getenv('REMOTE_ADDR'); 
		$host = gethostbyaddr($ip); 
	}
     $fd = fopen ("$logfile", "a+");
     fwrite ($fd,"Hacking attempt detected on " . $time . " by " . $ip . " (" . $host . ")\n");
     die("Hacking attempt detected, script execution will not continue and attempt was logged.");
   }
   die("Hacking attempt detected, script execution will not continue.");
}
// End security patch

$account = $_POST['account'];
$email = $_POST['email'];

$i=0;
if (isset($_POST['submit'])){
 // Get all accounts out of accounts.scp and put them into $accounts
 
 if (($account=="")||($email=="")){
    die("A field was left empty");
 } else {
   if(eregi("[\\]|\[|\]|\?",$account)){
      die("There are illegal characters in your account name.");
   }
   
   if(eregi("^[a-z0-9\._-]+@+[a-z0-9\._-]+\.+[a-z]{2,3}$", $email)){
     
    } else {
           die("Email is in an invalid format");
    } 

    while ($i<=count($bannedhosts)){
      if (stristr($email,$bannedhosts[$i])){
            die("Sorry, we can not accept email accounts from $bannedhosts[$i].");
      }
      $i++;
    }
   
 }

 $account = strtolower($account); // lowercase entered account
 $account = str_replace(" ","",$account); // remove spaces
 
 $i = 0;

 // read existing accounts into $accounts
 $fd = file ($sphereaccu);
 while ($i<=count($fd)){
  if (stristr($fd[$i], "[")){
     $fd[$i]=trim($fd[$i]);
     $fd[$i]=strtolower($fd[$i]);
     array_push ($accounts, $fd[$i]);
  }
 $i++;
 }

 // read existing emails into $emails
 $i=0;
 while ($i<=count($fd)){
  if (stristr($fd[$i], "EMAIL=")){
     $fd[$i]=trim($fd[$i]);
     $fd[$i]=strtolower($fd[$i]);
     array_push ($emails, $fd[$i]);
  }
 $i++;
 }

 // read accounts awaiting to be activated into $accounts
 $fd = file ($sphereacct);
 $i=0;
 while ($i<=count($fd)){
  if (stristr($fd[$i], "[")){
     $fd[$i]=trim($fd[$i]);
     $fd[$i]=strtolower($fd[$i]);
     array_push ($accounts, $fd[$i]);
  }
 $i++;
 }

 // read more emails into $emails
 $i=0;  // reset counter for next file
 while ($i<=count($fd)){
  if (stristr($fd[$i], "EMAIL=")){
     $fd[$i]=trim($fd[$i]);
     $fd[$i]=strtolower($fd[$i]);
     array_push ($emails, $fd[$i]);
  }
 $i++;
 }

 // look for entered account name
 $b=0;
 $result=1;
 while ($b<=count($accounts)){
 $account2="[" . $account . "]";
 if ($accounts[$b]==$account2){
     echo "$error_account";
     $b=count($accounts)+1;
     $result="no";
   }else{
       $b++;
   }
 }

 // check emails :)
 $b=0;
 while ($b<=count($emails)){
 $email2="email=" . $email . "";
 if ($emails[$b]==$email2){
     echo "$error_email";
     $b=count($emails)+1;
     $result=0;

    }else{
       $b++;
    }
 }

 if ($result){
   $fd = fopen ($sphereacct, "a+");
   fwrite ($fd,"\n[" . $account . "]\n");
   fwrite ($fd,"PASSWORD=" . $password . "\n");
   fwrite ($fd,"EMAIL=" . $email . "\n");
   fwrite ($fd,"FIRSTCONNECTDATE=" . $time . "\n");
   fwrite ($fd,"LASTCONNECTDATE=" . $time . "\n");
   fwrite ($fd,"\n");
   if ($useemail){
     mail("$email","Your $shardname Account","$email_body","From: $shardname Account Creator <$shardemail>");
   }
   if ($keeplog){
     $fd = fopen ("$logfile", "a+");
     fwrite ($fd,"" . $account . " was created on " . $time . " by " . $ip . " (" . $host . ")\n");
   }
   print_sucess();
 } else {
   print_form();
 }

}else{
 print_form();
}

?>

</BODY>
</HTML>
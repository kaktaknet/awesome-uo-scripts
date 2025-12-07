<?php
require "config.php";
require "smtp.php";
?>
<HTML>
<HEAD>
</HEAD>
<BODY>

<?php

if ($submit){
// Get all accounts out of accounts.scp and put them into $accounts

if (($account=="")||($email=="")){
   die("A field was left empty");
} else {
  if(eregi("^[a-z0-9\._-]+@+[a-z0-9\._-]+\.+[a-z]{2,3}$", $email)){
    
   } else {
          die("Email is in an invalid format");
   }
  
}

$account = strtolower($account); // lowercase entered account
$account = str_replace(" ","",$account); // remove spaces

$i=0;  // counter for reading file lines
$token = array("a","b","c","d","e","f","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9");
$password= $token[rand(0, 35)] . $token[rand(0, 35)] . $token[rand(0, 35)] . $token[rand(0, 35)] . $token[rand(0, 35)] . $token[rand(0, 35)]; // generate password
$emails = array("root@127.0.0.1");

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
//$fd = file ($sphereacct);
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
$result="ok";
while ($b<=count($accounts)){
$account2="[" . $account . "]";
if ($accounts[$b]==$account2){
    echo "$error_account<BR><BR>";
    print_form();
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
    echo "$error_email<BR><BR>";
    print_form();
    $b=count($emails)+1;
    $result="no";

   }else{
      $b++;
   }
}

if ($result=="ok"){
  $fd = fopen ($sphereacct, "a+");
  fwrite ($fd,"\n[" . $account . "]\n");
  fwrite ($fd,"PASSWORD=" . $password . "\n");
  fwrite ($fd,"EMAIL=" . $email . "\n");
  fwrite ($fd,"\n");
  $smtp=new smtp_client(); 
  $smtp->email("noreply@somewhere.com", $email, $email, $header[0], "Your $shardname Account!", $email_body);
  $smtp->send(); 
  print_sucess();

?>

<?
}

}else{
 print_form();
}
?>

</BODY>
</HTML>
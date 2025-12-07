<?php

$shardname = "Paradoxis";

$shardweb = "http://paradoxis.shorturl.com";

$sphereaccu = "C:\\sphere\\accounts\\sphereaccu.scp";

$sphereacct = "C:\\sphere\\accounts\\sphereacct.scp";

// Location of your smtp server (ask your ISP)
$smtp_server = "";

$accounts = array("[eof]","[admin]","[add]","[update]","[unused]","[.]"); // array of known accounts

$error_account = "Sorry, this account exists or is illegally named.";

$error_email = "Sorry, this email is in use on this shard.";

$email_body="Thanks for joining $shardname!\n\n Account: $account \n Password: $password\n\n Please visit the website ($shardweb) to get the required files and information on how to connect (new player page).
\n\n\n If you have received this message in error, it means someone is using this email address to register;  Please disregard this message and accept our apologies.";

// ADVANCED OPTIONS, SEE DOCUMENTATION

function print_sucess(){
?>
<B>Account created!</B><BR><BR>
Your account has been created and the password has been sent to the email address you provided.  You may want to head over to the downloads area and pick up the required files while waiting for your account to be activated.
<BR><BR>
Notes:
<UL>
<LI>Accounts are updated every 5 minutes, so if you cannot log in, try back again in 5 minutes.</LI>
<LI>All Accounts not used in 30 days/unused accounts are deleted periodically so login to your account as soon as you can after you receive your login information.</LI>
<LI>Thank you for joining our shard.</LI>

<?
}

function print_form(){
?>
<TABLE>
<TR><TD><FORM NAME="signup" METHOD="POST" ACTION="acctmgr.php">

<FONT>Account Name:</FONT></TD><TD><INPUT TYPE="text" NAME="account"></TD></TR>
<TR><TD><FONT>Email:</FONT></TD><TD><INPUT TYPE="text" NAME="email"></TD></TR>
<TR><TD><INPUT TYPE="submit" NAME="submit" VALUE="Create"></TD><TD></TD></TR>
<TR><TD></FORM></TD><TD></TD></TR>
</TABLE><BR>
<FONT COLOR="red">Your email is required for verification purposes only and will not be used for anything else.</FONT><BR><BR>
If there are spaces in your account name, they will be removed so "john smith" would become "johnsmith"<BR><BR>

<?

}

?>
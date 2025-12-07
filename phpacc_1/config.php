<?php

// General Configuration
// =====================

// Your shard's name
$shardname = "Your Shard's Name";

// Your shard's webpage
$shardweb = "http://url.to.your.shard.com";

// The shard Admin's email
$shardemail = "me@somewhere.com";

// location to sphereaccu.scp (remember to double escape \'s (\\)
$sphereaccu = "C:\\sphere\accounts\\sphereaccu.scp";

// location to sphereacct.scp (remember to double escape \'s (\\)
$sphereacct = "C:\\sphere\accounts\\sphereacct.scp";

// keep a log file? 1=yes, 0=no
$keeplog = 1;

// Location of log file (if you are keeping one; be sure to double escape \'s (\\))
$logfile = "accounts.log";

// known accounts, add to list if you have certain names you don't want used
$accounts = array("[administrator]","[eof]","[admin]","[add]","[update]","[unused]","[.]");

// On-screen error message displayed when there is an account name error
$error_account = "Sorry, this account exists or is illegally named.<BR>";

// On-screen error message displayed when there is an email duplication error
$error_email = "Sorry, this email is in use on this shard.";

// Email Configuration
// ===================

// use the email feature? 1 = yes, 0 = no; be sure to have your mail() function setup with PHP.
// if you are unsure how to do this, consult the documentation on php.net.
$useemail = 1;

// Array of banned email hosts.  To use, simply uncomment this variable (remove //'s) and add/remove hosts
// following the pattern as you desire. 
// $bannedhosts = array("hotmail.com","hotmail.co.uk","yahoo.com","yahoo.co.uk");

// Actual body of email message, needed only if you're using email feature
//
// VARIABLES:
// $shardname = your shard's name as defined above.
// $shardweb = your shard's website as defined above.
// $account = account name.
// $password = system generated password.

$email_body="Thanks for joining $shardname!\n\n Account: $account \n Password: $password \n\n Please visit the website ($shardweb) to get the required files and information on how to connect (new player page).
\n\n\n If you have received this message in error, it means someone is using this email address to register;  Please disregard this message and accept our apologies.";

// called when the account is created successfully, change depending on whether you're using email or not
function print_sucess(){
GLOBAL $password, $account; // Leave this line alone as it allows you to use those two variables!!!
?>
<B>Account created!</B><BR><BR>
Your account has been created.  You may want to head over to the downloads area and pick up the required files while waiting for your account to be activated.<BR><BR>

<BR>
Notes:
<UL>
<LI>Accounts are updated every 5 minutes, so if you cannot log in, try back again in 5 minutes.</LI>
<LI>All Accounts not used in 30 days/unused accounts are deleted periodically so login to your account as soon as you can after you receive your login information.</LI>
<LI>All transactions through this utility are logged.</LI>
<LI>Thank you for joining our shard.</LI>



<?
}

// MISC CONFIGURATION
// ==================

// function called when we first load page or when there is an error, defines the input form.
function print_form(){
?>
<TABLE>
<TR><TD><FORM NAME="signup" METHOD="POST" ACTION="index.php">

<FONT>Account Name:</FONT></TD><TD><INPUT TYPE="text" NAME="account"></TD></TR>
<TR><TD><FONT>Email:</FONT></TD><TD><INPUT TYPE="text" NAME="email"></TD></TR>
<TR><TD><INPUT TYPE="submit" NAME="submit" VALUE="Create"></TD><TD></TD></TR>
<TR><TD></FORM></TD><TD></TD></TR>
</TABLE><BR>

<UL>
<LI>Your email is required for verification and support purposes.</LI>
<LI>Spaces in account names will be removed: so "john smith" would become "johnsmith."</LI>
<LI>The characters [, ], ?, and \ are invalid and will be rejected.</LI>
<LI>All functions of this signup program are logged along with your IP address and hostmask for both our and your security.</LI>
</UL>

<?

}

?>
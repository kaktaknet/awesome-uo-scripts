<?php
include('conf.inc.php');
include('languages/'.$lang.'/lang.inc.php');
$gun = array (
0 => "Pazar",
1 => "Pazartesi",
2 => "Salý",
3 => "Çarþamba",
4 => "Perþembe",
5 => "Cuma",
6 => "Cumartesi",
);
$ay = array (
1 => "Ocak",
2 => "Þubat",
3 => "Mart",
4 => "Nisan",
5 => "Mayýs",
6 => "Haziran",
7 => "Temmuz",
8 => "Aðustos",
9 => "Eylül",
10 => "Ekim",
11 => "Kasým",
12 => "Aralýk",
);
$tarih = date('d ') . $ay[date('n')] . date(' Y ') .  $gun[date('w')] . date(' H:i:s');
function gen_rand_string($hash)
{
	$chars = array('1', '2', '3', '4', '5', '6', '7', '8', '9', '0');
	
	$max_chars = count($chars) - 1;
	srand( (double) microtime()*1000000);
	
	$rand_str = '';
	for($i = 0; $i < 8; $i++)
	{
		$rand_str = ( $i == 0 ) ? $chars[rand(0, $max_chars)] : $rand_str . $chars[rand(0, $max_chars)];
	}

	return ($rand_str);
}
if ($HTTP_GET_VARS[app] == 'new') {
include('languages/'.$lang.'/ust.inc.php');
include('languages/'.$lang.'/new.inc.php');
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if ($HTTP_POST_VARS[app] == 'newacc') {
if ($HTTP_POST_VARS[pass] != $HTTP_POST_VARS[pass2]) {
include('languages/'.$lang.'/ust.inc.php');
echo $text1;
include('languages/'.$lang.'/alt.inc.php');
exit;
} 
if (!ereg ("([a-zA-Z0-9]{3,8})", $HTTP_POST_VARS[pass], $regs)) {
echo $text2;
exit; 
}
if (file_exists($sphere.'\\accounts\\unactive\\'. $HTTP_POST_VARS[user])) {
include('languages/'.$lang.'/ust.inc.php');
echo $text3;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if (file_exists($sphere.'\\accounts\\active\\'. $HTTP_POST_VARS[user])) {
include('languages/'.$lang.'/ust.inc.php');
echo $text3;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if (file_exists($sphere.'\\accounts\\mails\\'. $HTTP_POST_VARS[mail] . '.mail')) {
include('languages/'.$lang.'/ust.inc.php');
echo $text4;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
$user_actkey = gen_rand_string(true);
$key_len = 54 - ( strlen($server_url) );
$key_len = ( $key_len > 6 ) ? $key_len : 6;
$user_actkey = substr($user_actkey, 0, $key_len);
$akt = $user_actkey;
$to  = $HTTP_POST_VARS[mail];
$subject = $text7;
$message = '<html>'.$text8.'<br>
'.$text9.':' . $HTTP_POST_VARS[user] . '<br>
'.$text10.':' . $HTTP_POST_VARS[pass] . '<br>
<br>
'.$text11.'<br>
<a href="'.$weburl.'acc.php?app=active&no=' . $akt . '">'.$weburl.'acc.php?app=active&no=' . $akt . '<\a>';
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-type: text\html; charset=windows-1254\r\n";
$headers .= "From:".$servername." <".$mailadress.">\r\n";
if ($mailuse == 'on') {
if (!mail($to, $subject, $message, $headers)) {
include('languages/'.$lang.'/ust.inc.php');
echo $text12;
include('languages/'.$lang.'/alt.inc.php');
exit; 
}
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $message;
include('languages/'.$lang.'/alt.inc.php');
}
include('languages/'.$lang.'/ust.inc.php');
if ($mailuse == 'on') {
echo $text5;
}
include('languages/'.$lang.'/alt.inc.php');
$fp = fopen($sphere.'\\accounts\\activation\\'. $akt, 'w');
fwrite($fp,$HTTP_POST_VARS[user]);
fclose($fp);
mkdir ($sphere.'\\accounts\\unactive\\' . $HTTP_POST_VARS[user], 0700);
$fp = fopen($sphere.'\\accounts\\unactive\\' . $HTTP_POST_VARS[user] . '\\' . 'mail', 'w');
fwrite($fp,$HTTP_POST_VARS[mail]);
fclose($fp);
$fp = fopen($sphere.'\\accounts\\unactive\\' . $HTTP_POST_VARS[user] . '\\' . 'fmail', 'w');
fwrite($fp,$HTTP_POST_VARS[mail]);
fclose($fp);
$fp = fopen($sphere.'\\accounts\\unactive\\' . $HTTP_POST_VARS[user] . '\\' . 'hist', 'w');
fwrite($fp,$tarih.' - '.$text6 .' '.$text10.':'.$HTTP_POST_VARS[pass] . '<br>');
fclose($fp);
$fp = fopen($sphere.'\\accounts\\unactive\\' . $HTTP_POST_VARS[user] . '\\' . 'pass', 'w');
fwrite($fp,$HTTP_POST_VARS[pass]);
fclose($fp);
$fp = fopen($sphere.'\\accounts\\unactive\\' . $HTTP_POST_VARS[user] . '\\' . 'plevel', 'w');
fwrite($fp,'1');
fclose($fp);
$fp = fopen($sphere.'\\accounts\\mails\\'. $HTTP_POST_VARS[mail] . '.mail', 'w');
fwrite($fp,$HTTP_POST_VARS[user]);
fclose($fp);
$fp = fopen($sphere.'\\accounts\\fmails\\'. $HTTP_POST_VARS[mail] . '.mail', 'w');
fwrite($fp,$HTTP_POST_VARS[user]);
fclose($fp);
exit;
}
if ($HTTP_GET_VARS[app] == 'active') {
$fd = fopen ($sphere.'\\accounts\\activation\\' . $HTTP_GET_VARS[no], "rb");
$user = fread ($fd, filesize ($sphere.'\\accounts\\activation\\' . $HTTP_GET_VARS[no]));
fclose ($fd);
if (file_exists($sphere.'\\accounts\\active\\'. $user)) {
include('languages/'.$lang.'/ust.inc.php');
echo $text13.'<br>'.$text14.'<\br>';
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if (file_exists($sphere.'\\accounts\\unactive\\'. $user)) {
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $text13.'<br>'.$text14.'<\br>';
include('languages/'.$lang.'/alt.inc.php');
exit;
}
$user_actkey = gen_rand_string(true);
$key_len = 54 - ( strlen($server_url) );
$key_len = ( $key_len > 6 ) ? $key_len : 6;
$user_actkey = substr($user_actkey, 0, $key_len);
$pin = $user_actkey;
$fp = fopen($sphere.'\\accounts\\unactive\\' . $user . '\\' . 'pin', 'w');
fwrite($fp,$pin);
fclose($fp);
$fp = fopen($sphere.'\\accounts\\unactive\\' . $HTTP_POST_VARS[user] . '\\' . 'hist', 'w');
fwrite($fp,$tarih .' - '. $text15.'<br>');
fclose($fp);
$fd = fopen ($sphere.'\\accounts\\unactive\\' . $user . '\\mail', "rb");
$mail = fread ($fd, filesize ($sphere.'\\accounts\\unactive\\' . $user . '\\mail'));
fclose ($fd);
rename ($sphere.'\\accounts\\unactive\\'. $user,$sphere.'\\accounts\\active\\'. $user);
if ($mailuse == 'on') {
include('languages/'.$lang.'/ust.inc.php');
echo $text16.'<br>'.$text17;
include('languages/'.$lang.'/alt.inc.php');
}
$to  = $mail;
$subject = $text18;
$message = "<html>".$text8.'<br>'.$text9.': ' .$user.'<br>'.$text19.': '.$pin .'<br>'.$text20."<br></html>";
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-type: text\html; charset=windows-1254\r\n";
$headers .= "From:".$servername." <".$mailadress.">\r\n";
if ($mailuse == 'on') {
mail($to, $subject, $message, $headers);
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $message;
include('languages/'.$lang.'/alt.inc.php');
}
$fd = fopen ($sphere.'\\accounts\\active\\' . $user . '\\pass', "rb");
$ps = fread ($fd, filesize ($sphere.'\\accounts\\active\\' . $user . '\\pass'));
fclose ($fd);
$pass = ($ps + 75) * 2;
$accfile='

['. $user. ']
PASSWORD=' . $pass;
$fp = fopen($sphere.'\\accounts\\sphereacct.scp', 'a');
fwrite($fp,$accfile);
fclose($fp);
exit;
}
if ($HTTP_GET_VARS[app] == 'mpin') {
if ($mailuse == 'on') {
include('languages/'.$lang.'/ust.inc.php');
include('languages/'.$lang.'/mpin.inc.php');
include('languages/'.$lang.'/alt.inc.php');
exit;
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $text37;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if ($HTTP_POST_VARS[app] == 'mpin') {
if (file_exists($sphere.'\\accounts\\fmails\\'.$HTTP_POST_VARS[mail] . '.mail')) {
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $text21;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if (file_exists($sphere.'\\accounts\\active\\'. $HTTP_POST_VARS[user])) {
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $text22;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
$fd = fopen ($sphere.'\\accounts\\fmails\\'.$HTTP_POST_VARS[mail] . '.mail', "rb");
$user = fread ($fd, filesize ($sphere.'\\accounts\\fmails\\'.$HTTP_POST_VARS[mail] . '.mail'));
fclose ($fd);
if ($user != $HTTP_POST_VARS[user]) {
include('languages/'.$lang.'/ust.inc.php');
echo $text23;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
include('languages/'.$lang.'/ust.inc.php');
$fp = fopen($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'hist', 'a');
fwrite($fp,$tarih . ' - '.$text36.'<br>');
fclose($fp);
if ($mailuse == 'on') {
echo $text24;
}
$fd = fopen ($sphere.'\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\pin', "rb");
$pin = fread ($fd, filesize ($sphere.'\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\pin'));
fclose ($fd);
include('languages/'.$lang.'/alt.inc.php');
$to  = $HTTP_POST_VARS[mail];
$subject = $text18;
$message = '<html>'.$text8.'<br>
'.$text9.': ' . $user . '<br>
'.$text19.': ' . $pin .'<br>
'.$text20.'<br><html>';
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-type: text\html; charset=windows-1254\r\n";
$headers .= "From:".$servername." <".$mailadress.">\r\n";
if ($mailuse == 'on') {
mail($to, $subject, $message, $headers);
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $message;
include('languages/'.$lang.'/alt.inc.php');
}
}
if ($HTTP_GET_VARS[app] == 'cpass') {
include('languages/'.$lang.'/ust.inc.php');
include('languages/'.$lang.'/cpass.inc.php');
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if ($HTTP_POST_VARS[app] == 'cpass') {
if (file_exists($sphere.'\\accounts\\active\\'. $HTTP_POST_VARS[user])) {
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $text25;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if ($HTTP_POST_VARS[pass] != $HTTP_POST_VARS[pass2]) {
include('languages/'.$lang.'/ust.inc.php');
echo $text1;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if (!ereg ("([a-zA-Z0-9]{3,8})", $HTTP_POST_VARS[pass], $regs)) {
echo $text2;
exit; 
}
$fd = fopen ($sphere.'\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\pin', "rb");
$pin = fread ($fd, filesize ($sphere.'\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\pin'));
fclose ($fd);
if ($pin != $HTTP_POST_VARS[pin]) {
include('languages/'.$lang.'/ust.inc.php');
echo $text26;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
include('languages/'.$lang.'/ust.inc.php');
echo $text27;
include('languages/'.$lang.'/alt.inc.php');
$fp = fopen($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'hist', 'a');
fwrite($fp,$tarih.' - '.$text28 .' '.$text10.':'.$HTTP_POST_VARS[pass] . '<br>');
fclose($fp);
$fp = fopen($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'pass', 'w');
fwrite($fp,$HTTP_POST_VARS[pass]);
fclose($fp);
$pass = ($HTTP_POST_VARS[pass] + 75) * 2;
$accfile='

['. $user. ']
PASSWORD=' . $pass;
$fp = fopen($sphere.'\\accounts\\sphereacct.scp', 'a');
fwrite($fp,$accfile);
fclose($fp);
exit;
}
if ($HTTP_GET_VARS[app] == 'admin') {
include('languages/'.$lang.'/ust.inc.php');
include('languages/'.$lang.'/admin.inc.php');
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if ($HTTP_POST_VARS[app] == 'apanel') {
if (file_exists($sphere.'\\accounts\\active\\'. $HTTP_POST_VARS[auser])) {
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $text29;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
$fd = fopen ($sphere.'\\accounts\\active\\'.$HTTP_POST_VARS[auser] . '\\pass', "rb");
$apass = fread ($fd, filesize ($sphere.'\\accounts\\active\\'.$HTTP_POST_VARS[auser] . '\\pass'));
fclose ($fd);
if ($apass != $HTTP_POST_VARS[apass]) {
include('languages/'.$lang.'/ust.inc.php');
echo $text25;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
if (file_exists($sphere.'\\accounts\\active\\'. $HTTP_POST_VARS[auser] . '\\plevel')) {
$fd = fopen ($sphere.'\\accounts\\active\\'.$HTTP_POST_VARS[auser] . '\\plevel', "rb");
$plevel = fread ($fd, filesize ($sphere.'\\accounts\\active\\'.$HTTP_POST_VARS[auser] . '\\plevel'));
fclose ($fd);
if ($plevel < '6') {
include('languages/'.$lang.'/ust.inc.php');
echo $text30;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $text30;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
include('languages/'.$lang.'/ust.inc.php');
include('languages/'.$lang.'/apanel2.inc.php');
include('languages/'.$lang.'/alt.inc.php');
}
if ($HTTP_POST_VARS[app] == 'apanel2') {
if (file_exists($sphere.'\\accounts\\active\\'. $HTTP_POST_VARS[user])) {
} else {
include('languages/'.$lang.'/ust.inc.php');
echo $text22;
include('languages/'.$lang.'/alt.inc.php');
exit;
}
include('languages/'.$lang.'/ust.inc.php');
include('languages/'.$lang.'/apanel3.inc.php');
if (file_exists($sphere.'\\accounts\\active\\'. $HTTP_POST_VARS[user] . '\\hist')) {
include($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'hist');
}
include('languages/'.$lang.'/alt.inc.php');
}
if ($HTTP_POST_VARS[app] == 'apanel3') {
if ($HTTP_POST_VARS[yasak]) {
if (file_exists($sphere.'\\accounts\\active\\'. $HTTP_POST_VARS[user] . '\\block')) {
unlink($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\block');
$accfile='

['.$HTTP_POST_VARS[user]. ']
BLOCK=0';
$fp = fopen($sphere.'\\accounts\\sphereacct.scp', 'a');
fwrite($fp,$accfile);
fclose($fp);
$fp = fopen($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'hist', 'a');
fwrite($fp,$tarih . ' - '.$HTTP_POST_VARS[auser].' '.$text31.'<br>');
fclose($fp);
} else {
$accfile='

['.$HTTP_POST_VARS[user]. ']
BLOCK=1';
$fp = fopen($sphere.'\\accounts\\sphereacct.scp', 'a');
fwrite($fp,$accfile);
fclose($fp);
$fp = fopen($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\block', 'w');
fwrite($fp,'block');
fclose($fp);
$fp = fopen($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'hist', 'a');
fwrite($fp,$tarih . ' - '.$HTTP_POST_VARS[auser].' '.$text32.'<br>');
fclose($fp);
}
$fp = fopen($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'hist', 'a');
fwrite($fp,$tarih . ' - '.$HTTP_POST_VARS[auser].' '.$text33.'<br>');
fclose($fp);
}
if ($HTTP_POST_VARS[plevel]) {
$fp = fopen($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'hist', 'a');
fwrite($fp,$tarih . ' - '.$HTTP_POST_VARS[auser].' '.$text34.' '. $HTTP_POST_VARS[pl] .' '.$text35.'<br>');
fclose($fp);
$fp = fopen($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'plevel', 'w');
fwrite($fp,$HTTP_POST_VARS[pl]);
fclose($fp);
$accfile='

['. $user. ']
PLEVEL=' . $HTTP_POST_VARS[pl];
$fp = fopen($sphere.'\\accounts\\sphereacct.scp', 'a');
fwrite($fp,$accfile);
fclose($fp);
}
include('languages/'.$lang.'/ust.inc.php');
include('languages/'.$lang.'/apanel3.inc.php');
if (file_exists($sphere.'\\accounts\\active\\'. $HTTP_POST_VARS[user] . '\\hist')) {
include($sphere.'\\accounts\\active\\' . $HTTP_POST_VARS[user] . '\\' . 'hist');
}
include('languages/'.$lang.'/alt.inc.php');
exit;
}
}
?>
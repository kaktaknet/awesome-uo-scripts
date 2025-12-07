<?php
$fd = fopen ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\pass', "rb");
$pass = fread ($fd, filesize ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\pass'));
fclose ($fd);
$fd = fopen ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\fmail', "rb");
$fmail = fread ($fd, filesize ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\fmail'));
fclose ($fd);
$fd = fopen ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\mail', "rb");
$mail = fread ($fd, filesize ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\mail'));
fclose ($fd);
if (file_exists('c:\\sphere\\accounts\\active\\'. $HTTP_POST_VARS[user] . '\\plevel')) {
$fd = fopen ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\plevel', "rb");
$plevel = fread ($fd, filesize ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\plevel'));
fclose ($fd);
} else {
$plevel = '-';
}$fd = fopen ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\pin', "rb");
$pin = fread ($fd, filesize ('c:\\sphere\\accounts\\active\\'.$HTTP_POST_VARS[user] . '\\pin'));
fclose ($fd);
if (file_exists('c:\\sphere\\accounts\\active\\'. $HTTP_POST_VARS[user] . '\\block')) {
$yasak = 'Lift ban';
} else {
$yasak = 'Ban';
}
echo $HTTP_POST_VARS[user].' Account details<br>
  <br>
  Þifre: '.$pass.'</p>
<p>Signing e-mail: '.$fmail.'</p>
<p>E-maili: '.$mail.'</p>
<p>Plevel: '.$plevel.'</p>
<p>PIN: '.$pin.'</p>
<form name="form1" method="post" action="acc.php">
  <p> 
    <input name="user" type="hidden" value="'.$HTTP_POST_VARS[user].'">  
    <input name="auser" type="hidden" value="'.$HTTP_POST_VARS[auser].'">
    <input name="apass" type="hidden" value="'.$HTTP_POST_VARS[apass].'">
    <input name="app" type="hidden" value="apanel3">
    Plevel: 
    <input name="pl" type="textfield" size="5" maxlength="1">
    <input name="plevel" type="submit" id="plevel" value="Deðiþtir">
  </p>
  <p> 
    <input name="yasak" type="submit" value="'.$yasak.'">
  </p>
  </form><br><br><br>';
?> 
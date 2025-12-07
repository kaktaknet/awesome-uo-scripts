<?php
echo 'Hesap bilgilerine bak<br>
<form name="form1" method="post" action="acc.php">
  <input name="user" type="textfield">
  <input name="auser" type="hidden" value="'.$HTTP_POST_VARS[auser].'">
  <input name="apass" type="hidden" value="'.$HTTP_POST_VARS[apass].'">
  <input name="app" type="hidden" value="apanel2">
  <input name="submit" type="submit" value="Bak">
</form>'
?>
<?php include('conf.inc.php');
 ?>
<form action="file:///C|/apache/htdocs/ist/languages/turkish/acc.php" method="post"><input name="app" type="hidden" value="newacc">
  <table width="468" border="0" cellspacing="0" cellpadding="2">
    <tr> 
      <td width="111"><font face="Arial, Helvetica, sans-serif">Username:</font></td>
      <td width="177"><font size="2" face="Arial, Helvetica, sans-serif">up to 14 chars long</font></td>
      <td width="180"><div align="left"><font face="Geneva, Arial, Helvetica, sans-serif"> 
          <input name="user" type="text" size="30" maxlength="14">
          </font></div></td>
    </tr>
    <tr> 
      <td><font face="Arial, Helvetica, sans-serif">Password:</font></td>
      <td><font size="2" face="Arial, Helvetica, sans-serif">3-8 chars long</font></td>
      <td><div align="left"><font face="Geneva, Arial, Helvetica, sans-serif"> 
          <input name="pass" type="password" size="30" maxlength="8">
          </font></div></td>
    </tr>
    <tr> 
      <td><font face="Arial, Helvetica, sans-serif">Password (again):</font></td>
      <td><font size="2" face="Arial, Helvetica, sans-serif">&nbsp;</font></td>
      <td><div align="left"><font face="Geneva, Arial, Helvetica, sans-serif"> 
          <input name="pass2" type="password" size="30" maxlength="8">
          </font></div></td>
    </tr>
    <tr> 
      <td><font face="Arial, Helvetica, sans-serif">E-mail</font></td>
      <td><font size="2" face="Arial, Helvetica, sans-serif">
	  <?php 
		if ($mailuse == "on") {
	  echo 'Activation code will sent to your e-mail.';
}
	  ?>
	  </font></td>
      <td><input name="mail" type="text" size="30" maxlength="100"></td>
    </tr>
    <tr> 
      <td colspan="3"><div align="center"><font face="Arial, Helvetica, sans-serif"></font><font size="2" face="Arial, Helvetica, sans-serif"></font> 
          <font face="Geneva, Arial, Helvetica, sans-serif"> 
          <input type="submit" name="Submit" value="Create account">
          </font></div></td>
    </tr>
  </table>
</form>
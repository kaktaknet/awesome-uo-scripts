Sphereserver Auto Account Creating System coded by Dagger
Used on Istiaron UO Shard of Turkey and found no bugs.

---*Updates in version 1.1*---
*Day and month names fixed. 
*Passwords are fixed.

---Installing---
*Copy all files to your PHP supporting web server running on same machine with your sphereserver.
*Edit conf.inc.php
*Edit files in languages\english as you want
*DO NOT edit acc.php if you dont know PHP well.
*Your account creation system is ready.

|---------------------------------------------------------------------------------------|
|NOTE: Old accounts cannot be accessed with this system unless you add them by yourself.|
|---------------------------------------------------------------------------------------|

---SMTP Server information---
Use a SMTP server if you want to send activation mails and other things.
Use a professional SMTP server which uses small amount of CPU and RAM. I prefer "QK SMTP Server".
---PHP Settings for SMTP server:
*Open php.ini
*find:
	[mail function]
	SMTP			=	localhost			;for win32 only
	sendmail_from	=	me@localhost.com	;for win32 only
*change localhost to your machine name.
*change me@localhost.com to your e-mail adress.

---Creating Language Packs---
-Example: To create a Russian Language Pack-
*Make a copy of languages\english folder
*Rename it to russian
*Translate all texts in files of russian folder
*Open conf.inc.php
*change $lang to 'russian'

|---------------------------------|
|Please send language packs to me.|
|---------------------------------|

---Contact---
dagger@dagger.istiaron.com
ICQ: 130013005
Miva Account Creation System Readme

Created by Warpe– Dragon
http://warped.ods.org
warped_dragon@hotmail.com
ICQ: 86428337
AIM: Warped Dragon
MSN: Use Email...
YIM: Not Telling

This system (and myself) assume that your running your sphere server in the folder c:\sphere, and that your running a Mivascript-enabled webserver on the same computer as the sphere. If this is not so, I suspect none of this will work....

The account.exe may require that you update your visual basic runtime files. These are available from the Microsoft Website:

http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=BF9A24F9-B5C5-48F4-8EDD-CDF2D29A79D5

This script will prevent players from creating accounts with duplicate IP's, Emails, and Names.


INSTALLATION: Place account.mv in your Miva Script folder. Be sure to edit the settings at the top. Once you've edited the variable that determines where the log file goes, place account.exe in the same folder as the log file. This will be somewhere in your Miva Data folder, I'm sure. Now, just add a link to account.mv on your website's join page. Thats it, your done!

USAGE: To use this system, simply have your players sign up for accounts using the account.mv form. This will create a logfile in whtever folder you specified. Every so often (I did it once a day), run account.exe. This will do several things. 

First, it will add to the file sphereacct.scp in the folder c:\sphere\accounts (I'm assuming you installed sphere in c:\sphere, if not this system will not work). The information added is all the new accounts from account.dat, and they will be added to the servers account files on the next restart, or if you force an account update via the console. 

The second thing this program will do is create a file on the desktop (c:\windows\desktop) called emails.txt. This is for email notification, just copy and paste each one and send it. You'll have to do this manually, at the time I didn't have a mail server to use for expirimenting with Miva's email sending functions. 

The third and final thing account.exe will do is rewrite account.dat and set all accounts in it to Active.

And thats it! Once installed, all you have to do is run the program once a day (or whenever...), and restart/force update your server. And send the emails, but that dosne't take to much time really...

Have fun!
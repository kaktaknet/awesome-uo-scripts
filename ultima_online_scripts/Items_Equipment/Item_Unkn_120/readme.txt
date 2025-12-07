Readme File for the MultiList UO Shard Tool (Beta Release 5)

Note: This is a Beta version.

You can find the latest version of this program at http://www.geocities.com/shadowlord13_1/

	---- Installation and Setup ----

The MultiList UO Shard Tool is coded in Java, using Java 1.3. 
To run it, it is recommended that you download the Java 1.3.1
JRE from http://java.sun.com, if you do not already have the
Java 1.3.1 JRE, JDK, or SDK.

Okay, assuming you have the 1.3.1 JRE installed, to get this set up:

First, extract everything in the zip file to a folder.
It doesn't really matter where you put it, it should work from anywhere.

	---- Running the Program  ----
	
Okay, now, there are two ways to run the program.
The first way is to double click run.bat. This will open a DOS prompt window
and display debugging output from the program to said window.
The second way is to double click MultiList.jar. 

If you run it from the Jar file, it will not show any windows at all, or
appear in the taskbar - It will be running silently. To close it, you'll
have to do ctrl-alt-del and find Javaw and close that. Or, when you shut down
your computer, it should close automatically.

	----  RegisterServers.ini  ----
	
When you run it for the first time, it will create a registerservers.ini file, and
write a some basic stuff to it, then it will exit. You should open this file,
and fill in the blanks. There will be comments in the file to explain what everything
does. If you don't want to fill something in, or don't need it (such as DynIp), you
can leave it blank.

Note that the file when it is initially written contains three RegisterServer lines, and three RegPass lines.
You can add more, and you can remove them, as well. 

There should be one RegPass per RegisterServer, and your first RegPass will be used on your first
RegisterServer, and so forth.

There is no limit to how many RegisterServers the program can connect to. 
Also, note the first RegisterServer line is set by default to the MPZ List Server
when the registerservers.ini is created, so you don't have to worry about setting that.

The second one is set by default to list.ultimaplayers.com, although this is in no way an indication
that their service actually works (AFAIK it doesn't ATM).

The third one is set by default to the OnlineUO shard list.

After you finish editing the file, and save it, you can start the program again. It
will read the file, remember what's in it, and will send out the information to the
registerservers you have listed. 

When it first starts, the program will send out the following information:
Name, RegPass, Port, Emu, Ver, TimeZone, Email, URL, Lang, CliVer, AccApp, DynIP.

It then requests the Accounts, Clients, Items, Chars, and Mem information
from Sphere, and immediately sends this information to the registerserver, and will
resend these every 30 minutes. (If there is no sphere server running on the computer
the program is running on and you have specified a DynIP, the program will attempt 
to connect to the server at the DynIP and get the information from it. If there is
no sphere server running there either, it will give up, and will proceed without
the Accounts, Clients, Items, Chars, and Mem information.)

NOTE: The program will NOT detect if you have changed your registerservers.ini and will NOT
reload it if you change it while it is running. If you change it, you will have to close and
re-start the program.

Since this is an Beta version, it is recommended that you run it by using run.bat, so that you
can see the debugging information.

At this time, the program does NOT write to a log file.

NOTE: The program currently cannot determine how many accounts you have. I have yet to find
a way to get Sphere to tell the program that.

	----  Compatibility Information  ----
	
This program was coded with the MPZ List Server in mind, and some features have been
added to the MPZ List Server specifically for this program.

Be aware that MPZ List Server is the only known list server to support Dynamic IP information.
If you have a dynamic IP, other list servers will probably not understand it.

This program sends your Dynamic IP information as a separate variable. The MPZ List Server supports
both this method, and the older method of placing the Dynamic IP in the URL field. Either will work
with the MPZ List Server. However, with other servers, only one method, or more likely neither, will work.

Also, it does not matter if you include HTTP:// in your URL in registerservers.ini. This program will handle
it just fine. (Sphere, however, doesn't send the URL if it begins with HTTP://).

NOTE: If your notes are over 1000 characters long, the MPZ List Server will only show all of your Notes on the
detailed information page about your shard. The list pages will only show the first 1000 characters of your Notes.
If anything else is over 255 characters, the MPZ List Server will truncate it. Other list servers may not.

	----  If you are NOT using Sphere  ----
	
AFAIK, no other servers will return the Accounts, Clients, Items, Chars, or Mem information 
when it is requested by this program.

This program attempts to connect to your shard and send the character 34. If you were running Sphere,
it would respond with:
Sphere, Name=SATest, Age=11, Clients=1, Items=7820, Chars=58, Mem=3292K
The line would end with a character 10 or 13 (It does not matter which, the program will work either way), and
then disconnect.

(Note that the clients information includes the connection from the program. The program decrements the returned value
by one so as to not count more clients than there really are.)

	----  If you are using Sphere  ----

It is recommended that you delete the registerserver= line from your Sphere.ini.
Please read this and the following section to see why.

Sphere has a limitation on the length of the Notes field. 
If you use Sphere to register with the list server, your notes may be cut off. 
If you remove your registerserver= line in Sphere.ini, and use this program and NOT Sphere, 
then you should have no problems, as this program is not subject to that limitation.

In addition, Sphere will NOT send any commas in your information. This program, however, encodes them
as another character, which the MPZ List Server will translate back into commas if they are in your
Notes field.

In other words, if you include commas in your Notes field, use this program to connect to the register server,
instead of Sphere, your commas will show up on the MPZ List Server.

Also, if you have HTTP:// in your URL, it will work fine with this program, but not with Sphere.

Other list servers do not (at this time) support the comma feature, but they should support the
unlimited notes field, and they will definitely work fine with the way this program handles HTTP
in the URL.

	----  Security Concerns with Sphere  ----
	
Damian of the Sphere Dev Team has stated that Sphere can release all the information in your sphere.ini file to
the registerserver. He has not stated when or why it does this, or whether the registerserver has to send something
to Sphere to make it do this.

While we have not detected any such thing happening, it may be a valid concern. 

This program has no such issue, and cannot release the information in your sphere.ini, because it does not read it.
This program will ONLY send the information I listed above, and, it will run
a separate thread for each registerserver you specify. Each thread can not and does not access the information
the others know. 

	----  General Security Concerns  ----
	
This program will NOT transmit information about what registerservers you have chosen to use.

You can specify a separate RegPass for each registerserver, and it is highly recommended that you do so.

This program will send each RegPass ONLY to the registerserver it is intended for.

If you add additional information to your registerservers.ini which the program does not expect, it will ignore it.

You can safely add as many comments (line beginning with //) as you want.

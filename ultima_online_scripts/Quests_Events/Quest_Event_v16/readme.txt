Thanks for your interest in my bounty system :)

Installation is very simple, just place the script file in your server's scripts directory.  If the server is running, simply do a /load C:\path\to\script\bountysystem.scp (the format is dependent on your setup and OS)

You will need to add the following code to your players as either an event, or at the bottom of the spheretables.scp file under the [skillclass 0] section:

ON=@Death
IF (<ACT.BRAIN>==0)&&(<SRC.MEMORYFINDTYPE.(0010).LINK>!=0)&&(<SRC.MEMORYFINDTYPE.(0010).LINK>!=<SRC.UID>)
 SRC.CONSUME i_bounty_deed
 SRC.NEWITEM i_bounty_deed
 SRC.ACT.LINK <SRC.MEMORYFINDTYPE.(0010).LINK>
 SRC.ACT.BOUNCE
ENDIF

To place in-game, do .add i_bounty_stone. Next link the stone(using the .link command and targeting the stone first then the board) to a bulletin board.  I suggest using a seperte bounty board for your system than the one that players can normally post messages on. 

When your players die, they get a bounty deed that can be taken to a bounty stone and the bounty be posted.

Well thats about it, if you have questions please post on the scriptsharing forum.
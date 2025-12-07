=================================================
	Context Menu for SPHERE 0.55+
             2002 OnlineUO.com

               Lead DEV Peter
=================================================



--===What's Context Menu===--
	The context menus is introduced on OSI since
the release of Client 3.0.3. It's intended to help
new players to understand and play UO easier than
before. This system will bring up a small menu
that contains useful available commands for a NPC
once the NPC is clicked by a player. For example,
if a player does a single click on a alchemist, a
menu similar to this will be shown to the client:

	------------------
	Open Paperdoll
	Buy
	Sell
	Train Alchemy
	Train Magery
	...
	------------------

The options in the context menu can replace the old
speech-trigger command, which is believed that it
will help players interact with NPCs.

--===The SPHERE Context Menu===--
	SPHERE does not support the client-side
triggered context menu so far (sphere99o). Since
it involve packet analyzing and core changing.
But with this script, SPHERE 55i+ can simulate
the context menu, and does no less than the OSI's
Original system.

--===Installing The Context Menu===--

	1) Extract the SPHEREChar_NPC.scp to the
	SPHERE Script directory, replace the old one

	2) Extract the #POD_SingleClick.scp to your
	sphere script directory.

	3) Reboot sphere, or in sphere console type
	LOAD /../#POD_SingleClick.scp, replace the /../
	with the relative or exact location of the script
	file. ie:
	LOAD Scripts/#POD_SingleClick.scp

	4) Resync if you did the LOAD method

--===Uninstalling the Context menu===--
	1) Replace the SPHERECHAR_NPC.SCP with the original
	copy

	2) Remove the #POD_SingleClick.scp

	3) Resync or Reboot SPHERE

--===Customizing the Context Menu===--
	
	With available commands, ADMINs can customize their 
own menu for a NPC, ie, a special quest that require speech
trigger that players usually don't use.

	1) TAG.Cmdx.DISP
	Syntax:
		TAG.cmd*.DISP = string
		Use under any tag-assign-able-procedure, ie.,
	@Create, @Click. Where the * is the Number *th command
	
	* from 1 -> 8
	
	Usage:
		Create a new option for the context menu, this
	tag tells the script what do display to the clients.
	it can be treated as the actual command which will be
	sent to the NPC if no other commands is specificed

	Example

	ON=@Create
	TAG.Cmd1.Disp = "Hire"
	Tag.Cmd2.Disp = "Train Swordsmanship"

	2) TAG.CMDx
	Syntax:
		Tag.Cmd* = "string"
		Where the * is the command number corresponding
	to the DISP command.

	Usage:
		This command is used when the .disp is not
	the actual command sent to the NPC. for example,
	the command Train MagicResistance is too long to
	put on the menu. So the one can use 
	"Train MagicResist" in the DISP line, and then in
	the CMD line, type in the actual command.

	Example
	TAG.CMD1.DISP = "Hire as Company"
	TAG.CMD1 = "Hire"
	TAG.CMD2.DISP = "Ask About: Where"
	TAG.CMD2 = "Where"
	TAG.CMD3.DISP = "Ask about: The Quest"
	TAG.CMD3 = "Quest"	//user speech trigger

	When player click on this npc, a context menu contains
	the following options will be shown:
	
	----------------------
	OPEN PaperDoll			//Default
	Hire As Company
	Ask About: Where
	Ask About: Quest
	----------------------

--===Pet Removing Property===--
	an APR (Automatic Pet Removing) function is included
	in this system as our clients request. The APR function
	will remove any pet that has a owner, and hasn't been
	mounted for a certain amount of time from the world.
	This feature will help most shards to reduce the world
	size. Since Mount-Storing is not possible in any case.
	
	All Pets that is assigned with the event e_horses will
	receive the APR function.

	to customize the APR timer, open the #POD_Singleclick.scp
	find this line:

	-------------------------------------
	findid.i_mount_remove.timer = 60 * 3
	-------------------------------------

	change the default 3 mins timer to whatever you like, and
	then, change this line as well:

	------------------------
	src.act.timer = 60 * 3
	------------------------

	If you want to disable the APR, remove the following lines
	in e_horses:
	
	------------------------
			if <findid.i_mount_remove>
				findid.i_mount_remove.timer = 60 * 3
			else
				src.newitem i_mount_remove
				src.act.layer = 30
				src.act.timer = 60 * 3
				src.act.update
				src.act.cont  = <UID>
			endif
	------------------------
	


--===Assigning Context Menu Properties===--

	All Default vendor NPCs had been assigned with
	the correct options with this release. If you have
	customized NPCs that need to use this system, assign
	the event e_Human_Environ to him.

	All Default Pets has been assigned with special
	Context menus that will only shown to the owner.
	If you have customized pets that need to use this
	feature, assign the pet with the event e_horses

--===Turning on\off the Menu===--
	
	Some clients may not like this feature, or GMs may
	want to turn this feature off. If so, use the command

	.SingleMenu
	
	to select either have this feature, or not.
	A system message will be shown to the client indicating
	their current Menu status.

--===Contact Information===--

	If you encountered any issues\problems with
this release, please contact:

Lead Dev Peter:
	ADMIN_Peter@Sympatico.ca

if the above email address does not work,
please visit out website at
	WWW.OnlineUO.com

===================================================================
	    =============================================
			2002 OSI VIRTUE SYSTEM
   		        FOR SPHERE SERVER

    		       A ONLINEUO PRODUCT
 		 BY LEAD DEV PETER & LEAD DEV BELGAR

		        VERSION 2.0 Beta
	    =============================================


--==SERVER VERSION REQUIREMENT==--
	This system is developed mainly for sphere 0.99l servers.
But it's proved that, after a series of simple tests, both SPHERE 0.55i
and SPHERE 0.99f can handle the dialogs and functions. 
	Since the new OSI dialogs, such as coloring Gump Items, needs
the newer client version's (3.0.6+, LBR\T2A\UOTD) support, these new 
dialogs will displayed as normal Gump Parts when running on 
SPHERE 0.99i- (Or with Client 3.0.6-).
	To run the virtue system on older client versions such as 3.0.0
and 2.0.3, the client side needs to patch the newer MUL file. Which can
be found in our support site : 
	-------------------------------------------------------
	Http://www.60yi.com/OnlineUO/ (http://www.OnlineUO.com)
	-------------------------------------------------------

NOTE: THIS SYSTEM WILL CAUSE MAJOR ERRORS WHEN RUNNING ON SPHERE 0.99m


--==VIRTUE SYSTEM INFO==--
	The Virtue system is part of OSI's LBR plan. It is said that
there are eight different virtues defined in the world of Britainnia
Players who pursue these virtues will gain some special abilities
such as self-resurrection.
	The full detailed information of the Virtue system can be
found at OSI's homepage, UO.com:
	------------------------------------
	http://update.uo.com/design_387.html
	------------------------------------

--==WHAT'S INCLUDED==--
	Virtue System Main Dialog
	The Virtue of Sacrifice	(OSI's first finished virtue)
	The Virtue of Compassion (Osi's Second Virtue)
	NPC Escort Quest : For The Virtue of Compassion (Released by OnlineUO)


--==INSTALLATION==--
	1. Unzip all scp files into your sphere's scripts directory
	2. reboot Sphere Server
	3. Your Players can now use .virtue command to view the main dialog

	--============--
	To use the NPC Escort Quest:
	In SPHEREITEMB6.scp, find [ITEMDEF 01e5e]. Then add these lines after the Defination Part:
	(after the line "DESCRIPTION=@")
	
	--------FOR SPHERE 0.99l+ -----------------
	ON=@UserDclick
		region.tag.bbsid	= <UID>
		return 0
	-------------------------------------------

	
	--------FOR SPHERE 0.99l- -----------------
	ON=@Dclick
		region.tag.bbsid	= <UID>
		return 0
	-------------------------------------------
	
	and then add these bulletin board ONE per city, double click them after you added them
	You can now setup spawn points for Escort Quest NPCs. They will post bulletin board msgs
	on the local bulletin board.

--==SUPPORT AND CONTACT INFO==--
	If you experienced any problem while using this
	system, or you have discovered some bugs. Please
	Contact:
	
	----------------
	Peter	: ADMIN_Peter@Sympatico.ca
	Belgar	: W.Arts1@chello.nl
	----------------



==========================================================================
		THANKS FOR CHOOSING ONLINEUO PRODUCTS
		     README BY LEAD DEV PETER
			  MAY 26th 2002





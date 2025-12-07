=====================================
	ONlineUO Golem Script
	     Version 2.1
             ADMIN Peter
             June 23 2002

           WWW.ONLINEUO.COM
=====================================


---Requirement---
SPHERE 55i +
OnlineUO Scripting Base Package


---===About Golem===---
	Iron Golem is introduced on OSI
in the year 2001. It's released with 
UOTD (Third Dawn), and availble in 2D LBR
with a new graphic. It is a mechanical
monster which spawns naturally around the 
world, and can be made by a Tinker with
some resources.
	To know more about the Iron Golem
please visit:

	UO Stratics Network---------------------------
	http://uo.stratics.com/hunters/irongolem.shtml
	----------------------------------------------

---===Installation===---

	1) UNZIP the .scp files into your
	script folder

	2) Find sphereskill.scp
	3) in sphereskill.scp, find:

	Indicate lines:----
	[SKILLMENU sm_parts]
	Parts
	-------------------

	add in:---------
	ON=i_Golem_Icon Golem
	SKILLMENU=sm_Tinker_Golem
	----------------
	after the indicated lines

	4)save the file
	5)if you don't have the iron golem def
	([CHARDEF 02F0]), then uncomment the
	def included in the script file, by 
	removing the "//" in front of the defination lines
	6)reboot sphere

---===To Make Iron Golem===---
	ou need power crystals,clockwork Assembly
	and eight gears.
	when tinkering = 100.0 you will have 50% chance
	of succeeding, and when tinkering = 0.0 you will have none
	the skill requirement is tinkiner = 90.0

	You need to spawn some Iron Golem around the world
	so your players can gather enough resources from these
	golems

	to use the command menu (activated when click on the golem)
	you need the OnlineUO Single Click Menu from our website
	and ask your client to use the command .singlemenu to choose
	to activate them.

	Without the command menu you can also order the golem by
	using speech commands:
	say 'REPAIR' to repair your golem
	and 'Self Destruct' to order your golem to destroy himself

---Contact information---
If you encountered any issues\problems with
this package, please contact:
Lead Dev Peter:
	ADMIN_Peter@Sympatico.ca
if the above email address does not work,
please visit out website at
	WWW.OnlineUO.com
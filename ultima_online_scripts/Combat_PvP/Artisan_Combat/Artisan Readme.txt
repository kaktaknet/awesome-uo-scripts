
  *******   ****   ********** **  ******  *******    ****     ** 
 **     **  **  **     **     **  **     **     **   ** **    ** 
 *********  **  **     **     **   **    *********   **  **   ** 
 ***   ***  ******     **     **    **   ***   ***   **   **  ** 
 **     **  **   **    **     **    **   **     **   **    ** ** 
 **     **  **    **   **     ** *****   **     **   **     **** 
================================================================
  A R T I S A N   v 0 . 7    b y   M a r o x
================================================================
Contact email : marox_gm@hotmail.com
================================================================
AIM : C1vilian
================================================================

			   [==Overview==]

This script generator is NOT intended for new scripters who don't know how to create their own weapons. This IS a script generator, its goal ISNT to create scripts easy, but to create huge amounts of CRAFTABLES faster than any other way. I hope this clears up.
I'd suggest its use on any and every shard, ofcourse, unless you want to do all the boring, long craftables work yourself *shrugs*.













[=======-Version History-========]


0.7 ------------------------
-Couple more weapons for blacksmithy, fixed Bows/Xbows formula.
-New menu access.
-Fixed "SKILL", not showing?
-Added the first version of the "Base Modifiers", Use explained below.
     ------------------------


0.6b ------------------------
-Added leather creation (supporting Hides, Skillmenus, Leather/Studded armor)
-Fixed "shieldbug" and "weaponbug" where shields would get badass AR and weapons big damage.
-Added a.. ehm, "nice" ascii text.
     ------------------------

0.5b ------------------------
-Added bowcraft creation (supporting Logs, Skillmenus, Regionsource, Bow/Xbows)
-Fixed message displaying v0.3
     ------------------------












The text below explains blacksmithy creation ONLY.

Leather creation is pretty much the same procedure as defined below and you shouldn't have any
problems with it.
The hides are outputted to item_ores.scp , armor to item_armors.scp and skillmenus to item_skillmenu.scp. The leather armors will use events-armors.ini if you have any.


------------------------------------

The text below explains blacksmithy creation ONLY.

Bowcrafting creation is pretty much the same procedure and you shouldn't have any
problems with it.
The logs and regionsource are outputted to item_ores.scp , bows/xbows to item_weapons.scp and skillmenus to item_skillmenu.scp
Bows/xbows will use events-weapons.ini if you have any.



===============[!NOTES!]===============












====[INTRODUCTION]====

Artisan is a program which can generate armors, weapons, ingots/ore/oreregion for them AND skillmenu's for crafting. Why have I made this when theres tons of other script generator programs around? Well, every single one I found didn't really make my craftable scripting life easier, as none supported skillmenus and most was a one-item generator as well. So, once again, this program generates whole sets of armors and weapons for them. Making blacksmithing (and some others) craftables much EASIER and FASTER to do.

How does it work?
-
Open the program and press 1 for blacksmithy creation. Then the program will ask you couple questions, let me explain them :

Name of armor : This is obviously the name of your armor AND weapons/ore/ingots. If you would do Silver as the armor name, it would come out like this :
Silver Platemail Helmet, Silver Katana, Silver Heater Shield, Silver Ingot, etc etc etc.

Enter skill to make((PLATEMAIL)) : this is the skill required for blacksmiths (obviously skill is blacksmithy) to create the PLATEMAIL set of this armor. Type in 90.5 for example, and a blacksmith with 90.5 blacksmithy and enough ingots will be able to craft the platemail set of this armor. Same goes for the other two skills (Chainmail armor sets, and ringmail armor sets.)
Additional notes :
Platemail means Full platemail set + Heater shield
Chainmail means Full chainmail set+Kite Metal Shield+Round Metal Shield Ringmail means Full ringmail set + Buckler Shield.

Enter Armor Defense : This is the armors defense(AR), type what you want the armors defense to be..
Note :
The defense differs for Chainmail, Ringmail, Platemail
You should give the most to Platemail, less to Chainmail, and the lowest to Ringmail. Ofcourse this order of AR is NOT required, just an example.

Enter Armor Color : This is the color the weapons/armor/ingots/ore will be.

Enter Armor Hitpoints : This is the armors hitpoints (durability)

Enter Ore Skill To Mine : This is how much mining will the player need to dig up the ore. (You might want to costumize this by yourself at the end.)

Include Weapons? : This is whether you want weapons or not. Type 1 for yes (Include weapons), type 0 for no (Do NOT include weapons)

If you decided to have weapons this question pops up : 
Highiest Weapon Damage : This is the highiest weapon damage, example : iron has 48, which means Halberds range from 4,48   Bardiches less, Vikings lesser, and Katanas even less.This is basically what highiest dmg will the hally have(highiest MAXDMG wep). Don't really know how to explain this but feel free to play with it around.
NOTE:  You MUST pick a number highier than 48 or ERRORS will occur.



FILE EXPLANATION:
Uppon completion of procedure you will find these new files that were created by the program :

item_armors.scp - The code for armors/shields will output here (Copy/Paste to whatever file you wanted this in.)


item_weapons.scp - The code for weapons will output here (Copy/Paste to whatever file you wanted this in.)- This will only appear if you choosed to create weapons as well.


item_ingots.scp - The code for ingots will output here (Copy/Paste ingots to sphereitem_ore.scp)


item_ores.scp - The code for ore will output here AS WELL as code for the regionsource (Copy/Paste ores to sphereitem_ore.scp, region source goes to sphereregion.scp - you might want to create the ore blocks with percentages so they can dig them up.)


item_skillmenu.scp - The code for skillmenus will output here - craftables (Carefully paste right blocks into sphereskill.scp.)




[==USE OF THE EVENT FILES==]

There are two more INI files that come with this package : 
events-weapons.ini and events-armors.ini
IF you do not have these or deleted them somewhy, just create two new blank .INI files with the same names. Why are they here? Well, if you want to costumize your weapons/armors a bit more, this is your solution. Events-Armors.ini is for ARMORS, while Events-Weapons.ini is for WEAPONS.
Example : You maybe want an armor that only good people can wear and weapons of the same kind that would deal extra damage. In that case you'd open up Events-Armors.ini and write this in :

ON=@EQUIP
IF (<SRC.KARMA> >= 5000)
RETURN 0
ELSE
RETURN 1

ON=@UNEQUIP
SRC.MESSAGE You are no longer protected by the heavens..

Note that there is NO limit on how many of these you can put in. These however will only be added to armors/shields. Then you would open Events-Weapons.ini, where you would type something like this in :

ON=@DAMAGE
SRC.HITS=<SRC.HITS> + -50
SRC.EMOTE being torn appart by the elven blade..

ON=@DCLICK
SRC.MESSAGE You are surrounded by healing winds..
SRC.HITS=<SRC.HITS> + 1
RETURN 1


-Like i said you can do an unlimited amount of these, be it whatever as long as it is a legal sphere command/event/whatever-







[==USING THE BASE MODIFIERS==]

New to version 0.7, there is a certain "basemod" directory that comes with Artisan.
Whats this? Well.. it probably is the answer to the only previous limitations in Artisan.
It allows you to change the base weapon attributes. Only WEIGHT (speed) is currently editable in 0.7, thats the only useful thing to modify anyway. How does it work? Open up any of the text files in the basemod directory. You'll see something like "WEIGHT=8". For example, open up the item_katana.txt and change the line to WEIGHT=1 . Well its not a smart move to give katana such speed but its just to show off whats it do.. now if you create the weapons, katana will have weight=1. This allows you to fully costumize Artisan's weapon generating. The default weapon weight is from the default sphere files, so yes, it is a Very good move to modify them, unless you want crappy SPHERE's speed..















Note that I do not take any resposibility for ANY damages or what ever this program causes to your computer. It was however tested on many computers. USE THIS PROGRAM AT YOUR OWN RISK!


===========================================================
Was this program useful to you?
If so, PLEASE send me an email!
I REALLY would like to see how many people find it useful.
Regards,
	Marox
===========================================================





---------------------------------------
   Files included in this package :

	Artisan Readme.txt
	Artisan.exe
	events-weapons.ini
	events-armors.ini
	basemod directory
---------------------------------------
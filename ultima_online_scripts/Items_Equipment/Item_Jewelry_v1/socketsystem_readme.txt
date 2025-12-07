-----------------------------------------------------
|                 Dawgy Presents:                   |
|                                                   |
|            The Socketed Item System               |
|                   Version 0.8                     |
|               dawgy@boxofhate.com                 |
-----------------------------------------------------

-------------------- 2003 | Dawgy | Use this script as you want, just don't steal credit for it :)
-------------------- i'd REALLY appreciate questions, bugs, requests, thank you's and hate mail at
-------------------- dawgy@boxofhate.com
-------------------- View bottom for changelog! :|

1.0 > About
-
Ever played Diablo 2? Remember the types of weapons that had sockets, where you could
insert gems and the weapon would increase in power according to the gem.
This system attempts to recreate that, with up to 1-5 sockets in each item, a tool to
insert them, with a nice dialog to view the item, add new gems to it, and view it's gem powers 
--
2.0 > Installing
-
First:  Plop it in your Spheredir/Scripts/custom directory.
Second: At the top of the file, there is a section called [DEFNAMES Socket_Settings] with the drop rate
of socketed weapons and gems, the higher the value, the rarer the drop. ( A value of 1=Always drop)
Third:  Add one of these events on each monster you want to drop a socketed weapon or gem

		EVENTS=+E_SOCKET_RANDOM_GEM			// The monster might drop a random gem

		EVENTS=+E_SOCKET_RANDOM_WEAPON			// The monster might drop a random socketed weapon
		EVENTS=+E_SOCKET_RANDOM_SWORD			// The monster might drop a random socketed sword
		EVENTS=+E_SOCKET_RANDOM_BOW			// The monster might drop a random socketed bow
		EVENTS=+E_SOCKET_RANDOM_MACE			// The monster might drop a random socketed mace
		EVENTS=+E_SOCKET_RANDOM_FENCING			// The monster might drop a random socketed fencing weapon

		EVENTS=+E_SOCKET_RANDOM_ARMOR			// The monster might drop a random socketed armor
		EVENTS=+E_SOCKET_RANDOM_ARMOR_LEGGING		// The monster might drop a random socketed legging
		EVENTS=+E_SOCKET_RANDOM_ARMOR_ARM		// The monster might drop a random socketed arm
		EVENTS=+E_SOCKET_RANDOM_ARMOR_GLOVE		// The monster might drop a random socketed glove
		EVENTS=+E_SOCKET_RANDOM_ARMOR_HELM		// The monster might drop a random socketed helm
		EVENTS=+E_SOCKET_RANDOM_ARMOR_CHEST		// The monster might drop a random socketed chest
		EVENTS=+E_SOCKET_RANDOM_ARMOR_GORGET		// The monster might drop a random socketed gorget

		EVENTS=+E_SOCKET_RANDOM_SHIELD			// The monster might drop a random socketed shield

		EVENTS=+E_SOCKET_RANDOM_SHIELD_3SOCKET		// The monster might drop any socketed shield ( 3 sockets )
		EVENTS=+E_SOCKET_RANDOM_SHIELD_4SOCKET		// The monster might drop any socketed shield ( 4 sockets )
		EVENTS=+E_SOCKET_RANDOM_SHIELD_5SOCKET		// The monster might drop any socketed shield ( 5 sockets )

		EVENTS=+E_SOCKET_RANDOM_WEAPON_3SOCKET		// The monster might drop any socketed weapon ( 3 sockets )
		EVENTS=+E_SOCKET_RANDOM_WEAPON_4SOCKET		// The monster might drop any socketed weapon ( 4 sockets )
		EVENTS=+E_SOCKET_RANDOM_WEAPON_5SOCKET		// The monster might drop any socketed weapon ( 5 sockets )

		EVENTS=+E_SOCKET_RANDOM_ARMOR_3SOCKET		// The monster might drop any socketed armor ( 3 sockets )
		EVENTS=+E_SOCKET_RANDOM_ARMOR_4SOCKET		// The monster might drop any socketed armor ( 4 sockets )
		EVENTS=+E_SOCKET_RANDOM_ARMOR_5SOCKET		// The monster might drop any socketed armor ( 5 sockets )

		EVENTS=+E_SOCKET_RANDOM_ITEM_3SOCKET		// The monster might drop anything socketed ( 3 sockets )
		EVENTS=+E_SOCKET_RANDOM_ITEM_4SOCKET		// The monster might drop anything socketed ( 4 sockets )
		EVENTS=+E_SOCKET_RANDOM_ITEM_5SOCKET		// The monster might drop anything socketed ( 5 sockets )

You could write your own item drop events if you wish, they are located on the bottom of 
the system file.
--
2.1 > Items, functions, Characters for use
-
Items:
1.  i_socket_tools						
	This is the tool to insert gems into socketed weapons
Functions:
1.  f_socket_create_gem_rand		
 	Creates a random gem
	USAGE : f_socket_create_gem_rand

2.  f_socket_create_gem				
	Example: f_socket_create_gem(3)
	Creates a gem of your choice 
	USAGE : f_socket_create_gem(GEMID)

3.  f_socket_create_weapon			
	Example: f_socket_create_weapon(1,4) || A random sword with four sockets
	Creates a random socketed weapon of your type choice 
	USAGE : f_socket_create_weapon(Type,Maxsockets) 
	Type= 0=Random 1=Sword 2=Bow 3=Axe 4=Mace 5=Fencing weapons 
	ATTN: Maxsockets can only be from 1 to 5, going over 5 WILL result in errors

3.  f_socket_create_armor
	Example: f_socket_create_weapon(5,3) || A random armor with three sockets
	Creates a random socketed armor of your type choice
	USAGE: f_socket_create_armor(Type,Maxsockets) 
	Type= 0=Random 1=Leggings 2=Arms 3=Gloves 4=Helmet/Coif 5=Chest 6=Gorget  
	ATTN: Maxsockets can only be from 1 to 5, going over 5 WILL result in errors

4.  f_socket_create_shield
	Example: f_socket_create_shield(4) || A random shield with four sockets
	Creates a random shield
	USAGE: f_socket_create_shield(Maxsockets)
	ATTN: Maxsockets can only be from 1 to 5, going over 5 WILL result in errors

5.  f_socket_create_item
	Example 1: f_socket_create_item(i_sword_viking,5) || A Viking sword with five sockets
	Example 2: f_socket_create_item(i_sword_viking_vanq,3) || A Viking sword of vanquishing with three sockets
	Example 3: f_socket_create_item(i_platemail_chest,4) || A Platemail chest with four sockets
	Creates a socketed item of your choice, with more control of what the item will be
	USAGE : f_socket_create_item(Type,Maxsockets) Type= 
	itemdef for item, or a defname array, such as RND_AXE, RND_SWORD , RND_BOW, RANDOM_CHEST_ARMOR, i_platemail_chest etc.
	ATTN:Maxsockets can only be from 1 to 5, going over 5 WILL result in errors

Characters:
1. c_socket_test_guy
	Just an orc with ALL the drop events set on him by default, you could use it
	to try out your socketed item and gem drop rate (Caution, lots of events! :P)
							
3.0 > Customizing 
-
The system is quite customizable, and you can easily write new gems. For each gem, there are 6-8 definitions, and one typedef(event)
--
3.1 > Adding new gems ( With NON-stackable powers, meaning that the user cannot have more than one of the gem socketed in each item )
-
First, to add a new gem, you'll have to go to the section called [DEFNAMES Gems], and add five new defnames.. 
Like so:
	MYGEM_Gem_Name			The New Improved Gem	// The name of the gem
	MYGEM_Gem_Events		t_Socket_Gem_MYEVENT	// The name of the event the gem will give the weapon (Can be anything)
	MYGEM_Gem_info			Adds +15 Strength	// A breif description of the gem powers, this will show in the gem info dialog
	MYGEM_Gem_special_tag[0]	0			// Are its powers stackable? 0=NO,1=YES || More on this in 3.2
	MYGEM_Gem_itemid		4			// How the gem will look like in the world | Gumps, See below for the colour list

			The *_Gem_itemid colour list :
			 0 = Dark blue/blackish
			 1 = Blue
			 2 = Green
			 3 = Orange
			 4 = Purple
			 5 = Red
			 6 = Light Blue
			 7 = Yellow/Goldish

All we've done is set a few variables, this generally stores all the information on this particular gem.
Its quite important that the first part of the defname (MYGEM in this case) to be identical to all of the gem variables
-
Now, lets add a new defname in the [DEFNAMES Gemarrays] section, scroll down to it and you'll see something like:

	[DEFNAMES Gemarrays] // socket_gem_array[GEMID] ____
	socket_gem_count		5	
	socket_gem_array[1]		Test
	socket_gem_array[2]		Test2
	socket_gem_array[3]		Test3
	socket_gem_array[4]		Test4
	socket_gem_array[5]		Test5

Add a defname to the bottom of it. In this case it will be:

	socket_gem_array[6]		MYGEM

AND, You must CHANGE the "socket_gem_count" to reflect the 
number of gems you have at your disposal. In this case it'll be

	socket_gem_count		6

Get it?. The "socket_gem_array[6]" is set to "MYGEM" to reflect the 
first part of the previous 5 defnames you just set earlier ( such as MYGEM_Gem_Name )
the "6" you set will be the GEM ID of the gem, (used mostly in scripts..)
-
Finally, we're going to write its TYPEDEF, Scroll down to a section called:
// -------------------------------[ TYPEDEFS, Powers added to items ]-------------------------------
There you will see various typedefs (i.e. item events) for various gems,
This section tells the system what each gem actually adds to the weapon.

Lets write the typedef for our new gem. Something like this:

	[TYPEDEF t_Socket_Gem_MYEVENT] 
	ON=@EQUIP 
	SRC.STR=<EVAL ((SRC.STR)+15)>  // +15 to strength when player equips
	ON=@UNEQUIP 
	SRC.STR=<EVAL ((SRC.DEX)-15)>  // -15 from strength when player unequips

Notice the name of the typedef must reflect what your "MYGEM_Gem_Events" is set to
We set it to "t_Socket_Gem_MYEVENT" earlier..
-

Thats it!, Your gem has been created and is ready for use, it automatically enters the
gem drop event and will be dropped at random by monsters that have the gem drop event.

You can test your specific gem by typing .f_socket_create_gem(6), 
You'll get your gem bounced to your pack and ready for insertion
( GEMID is 6 in this example, ( remember: socket_gem_array[GEMID] ) )
--
3.2 > Adding a new gem, with Stackable powers ( Player can have more than one gem of the same type in his item )
-
This time, we're going to create a stackable gem, so the player can have more than one of this particular gem in his item.
For this example, lets make a gem that adds +10 to Mana.. Create the first defnames in [DEFNAMES Gems] Like you did earlier for
the unstackable gem.

	Mana_Gem_Name			Gem of Mana		// The gem name
	Mana_Gem_Events			t_Socket_Gem_Mana	// the event name
	Mana_Gem_info			+10 Mana		// a Breif description of the gem powers
	Mana_Gem_special_tag[0]		1			// 0=No,1=Yes :: Does the item need a special tag? ( are the powers stackable? )
	Mana_Gem_special_tag[1]		STACK_ADD_MANA		// The tag itself (tag.STACK_ADD_MANA)
	Mana_Gem_special_tag[2]		10			// The value (How much it adds to the tag)
	Mana_Gem_itemid			1			// The gem id, selected from the socket_gem_baseid_dec array

You see there are two new defnames in this example, namely Test_Gem_special_tag[1] and Test_Gem_special_tag[2]
They're set to a TAG so the item will track how much its supposed to add/substract to the player

-
Add your gem to the socket_gem_array as before
-
Now for the typedef, take a look at this one

	[TYPEDEF t_Socket_Gem_Mana] 
	ON=@EQUIP 
	SRC.MAXMANA=<EVAL ((SRC.MAXMANA)+<TAG.STACK_ADD_MANA>)>  // Look at the STACK_ADD_MANA tag of the item, and add it to the players strength
	ON=@UNEQUIP 
	SRC.MAXMANA=<EVAL ((SRC.MAXMANA)-<TAG.STACK_ADD_MANA>)>  // the same, but remove the mana addition

Its done, the gem has been added, and now the player can put as many of these in his item.
-
Additionally, you could later create another gem that would also add to mana, but f.ex a different amount (+20)
Examples:

	MoreMana_Gem_Name		Gem of Greater Mana	
	MoreMana_Gem_Events		t_Socket_Gem_Mana	// It uses the same event as the last one
	MoreMana_Gem_info		+20 Mana					
	MoreMana_Gem_special_tag[0]	1							
	MoreMana_Gem_special_tag[1]	STACK_ADD_MANA		//It uses the same tag as the last one
	MoreMana_Gem_special_tag[2]	20			// Here's the amount it adds.
	MoreMana_Gem_itemid		3			// it can look different too :P											

Add your gem to the socket_gem_array as before
No need to add a new typedef, as we already have one! it uses the same one AND the same tag
---

Changelog 
> 0.8
+ Feel free to email me if you have suggestions or problems...
+ Socketed Armors. Socketed armor drops, etc.
+ Item specific gems: Armor only gems, Weapon only gems, Shield only gems and all around gems (That work in any of them)
+ New function: f_socket_create_armor(Type,Maxsockets), Explained in function list(readme).
+ New function: f_socket_create_shield(Maxsockets), Explained in function list(readme).

> 0.6.5
+ Changed function: f_socket_create_weapon2 is now f_socket_create_item(Type,Maxsockets), Explained in function list(readme). 

> 0.6
+ Second release
+ Now uses a memory object for dialogs instead of vars, i believe (correctly!)
- that using vars for them would easily mess things up quite a bit on large shards
- Sorry if you experienced errors :|

> 0.5.5
+ Changed the gem info dialog to include weither the gem is stackable or not
+ When you target a gem with the item socketer you'll get the gem info dialog.
+ Changed the Sample +Dex +Int gem boosts to be stackable :P

> 0.5 
+ First release

To do:
+ Armour socketing
+ Small, forgettable things :|


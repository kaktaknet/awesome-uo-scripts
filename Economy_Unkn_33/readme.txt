Vendor Rental System - version .1
*********************************

This script allows players to "rent" vendors in public spaces for a period of about 7 days at the cost of 15K. The script takes care of asigning a vendor to a player and removing that vendor when the "lease" has run out.  A warning (or feature?) to players is that once the lease has run out the vendor and all items/cash on him/her are deleted, and the shop is reset so that someone else can rent the shop.  The owner has the option, of course, to renew his lease at any time during the 7 day period by double-clicking the rental sign, and choosing the appropriate option.  Also available in this release is the option to change the vendor's name to a more descriptive name, or one you like.  I plan on adding more features as time permits :)

INSTALLATION
************

Installation simply involves placeing the included script in your scripts directory and loading it.  Then, go to places where you would like players to be able to place vendors and .add i_vendor_rental signs.  You may have to RESTART your server in order for the consumebank function to work properly (if you do not already have this function, please add it either to a seperate file or the bottom of the script file; it is of Amlaruil's creation and is found below.  If you are using my bounty system, you already have this function.)

Consumebank function (required; if you have my bounty system, you already have it)

	[FUNCTION consumebank]  //Thanks to Amlaruil for this!
	act=<SRC.FINDLAYER(layer_bankbox).uid> 
	act.layer=layer_pack 
	act.type=t_container 
	act.equip 
	src.consume <args> 
	act.layer=layer_bankbox 
	act.type=t_eq_bank_box 
	act.equip

MISC COMMENTS
*************
if for some reason you need to remove a vendor and reset a prticular lease,  just set its sign's timer to 1 and the vendor will disappear and all variables will be reset and ready for the next person.

To increase/decrease the lease time find the lines that read:
                                SRC.ACT.TIMER=60*60*24*7
and set the timer accordingly (default is about 7 days)

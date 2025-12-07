Readme for Cloud's Vendor System:

This is a vendor system made from the 0. It's fully and easily editable.
Almost everything are on the DEFs, including the txts, and messages.

You don't have to edit any script you have in the default script package, it overrides the default
i_vendor_deed.

If you don't have the i_vendor_deed for sale in your npcs, edit the SPHERETEMP_VEND.scp in your
scripts folder to make it buyable.



Some instructions:

1-If you set this def:

"vendorshop_onoff 0 ///<-- put 1 if you have a Vendor Shop"

to 1, you have to set this def here:

"shopname 'Mercado'"

to your vendors shop's name, to make the script able to create the vendor at the market.

AND of course, create the area in your sphere_map.scp!


2-If you don't want to use the vendor shop, you can use the players houses as the shop, to make it
just activate this def:

"vendoronhouse_onoff 1"

to 1.

NOTE about 1 & 2: Default in "vendorshop_onoff" is 0 (off), and in "vendoronhouse_onoff" is 1 (on)


3-Players can't put vendors too next to another vendor. The script blocks it. To less your lag, and
avoid players putting too much vendors in 1 tile.


4-Only ONE player can access the vendor at a time. If you're the owner, you'll automatically make
the player accessing the vendor close the dialogs and make it able for you to access the vendor.


5-You have 6 minutes to access the vendor, before it closes the dialogs.


6-To access the Buyer menu, just say "BUY" (the owner can't access this)


7-To access the owner menu, just say "STOCK"


8-I think the rest is self-explainable, you just have to look at the defs, there are a tip on how to
use each one of them, at their side.
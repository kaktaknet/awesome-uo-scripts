#prefix-local
#omit-original-code

#Definition tests

#Definitions:

#itemdef i_hide_dragon_white(i_hide)
#Compiles to:
#	[ITEMDEF i_hide_dragon_white]
#	ID=i_hide

#itemdef i_hide_dragon_white(01078)
#Compiles to:
#	[ITEMDEF i_hide_dragon_white]
#	ID=01078

#itemdef 0eed(i_gold):
#Compiles to:
#	[ITEMDEF 0eed]
#	DEFNAME=i_gold

#itemdef 0ffa(01)
#Compiles to:
#	[ITEMDEF 0ffa]
#	ID=01

#Either defnames or defname works here
defnames dam_flags:	#This is from sphere_d_events.scp in sphere 99u's scripts.
	
	#Technically, you only need one space, tab, or equals sign between the name and its value. 
	
	dam_god			=00001     #Unblockable "god" damage 
	dam_physical	=00002     #Some sort of physical damage (as opposed to magical) 
	dam_magic		=00004     #Some sort of magical damage 
	dam_poison		=00008     #Poisonous or biological (harm spell) damage 
	dam_fire		=00010     #Fire-based damage 
	dam_lightning	=00020     #Electrical damage (lightning) 
	dam_drain		=00040     #Draining damage 
	dam_general		=00080     #Damage that hits the entire body, rather than just one part of it 
	dam_acidic		=00100     #Acidic damage (will destroy armor) 
	dam_cold		=00200     #Cold-based damage 
	dam_slash		=00400     #Damage done by slashing (swords, etc)


#Either events or event works here
event e_undead: 
#(This is from sphere_d_events.scp in sphere 99u's scripts.	)

	#This def is a trigger. It can have ()s if you want, but they must be empty.
	def EnvironChange: #self is char
		#return(0)
		# Remove the first # in the line right above this one to disable this event. 
		# This event makes undead die without loot in a single hit during daylight hours.
		if ((sector.isdark) or (flags&(statf_nightsight|statf_indoors))):
			if not safe.tag.lightstr:
				return(0)
			anim(011)
			bark(4)
			str=safe.tag.lightstr	# restore me.
			hits=str
			tag.lightstr=0
			karma=safe.tag.lightkarma
			tag.lightkarma=			#just dispose of this.
			fame=safe.tag.lightfame
			tag.lightfame=
			flags=flags&~statf_conjured	#no loot if killed.
			return(0)
	
		# i can't live in light areas. weaken me ? or destroy me ?
		anim(014)
		bark(4)
		if safe.tag.lightstr:
			return(0)
		if (flags&statf_conjured):
			remove
			return(1)
		flags=flags|statf_conjured	#no loot if killed.
		tag.lightstr=str
		str=1
		hits=1	# very weak.
		tag.lightkarma=karma	# killing it means nothing now.
		karma=-2
		tag.lightfame=fame
		fame=10
		return(0)


#This was converted from a 55i script I made for Shattered Alliance. The dclick trigger was added for testing trigger
#generation.
itemdef i_hide_dragon_white(i_hide):
	name="White Dragon Hides"
	value=500
	weight=5
	CATEGORY="Items by Professions"
	SUBSECTION="Tanner"
	DESCRIPTION="Dragon Hides White (Pile)"

	def create: #src is char
		color=07a1
		amount=10
	def dclick: #src is char
		say("Your backpack's name is "+findlayer(21).name)

#Most of this was converted from sphere_d_char_lbr_new.scp in 99u's scripts. The death trigger was converted from
#a test fix I did for this, and the deathcorpse trigger was added to test getting the corpse's UID when something dies.
chardef 0B6(c_m_orc_bomber):
	name="Orcish Bomber"
	sound=snd_MONSTER_ORC1
	icon=i_pet_orc_lbr
	can=MT_WALK|MT_RUN|MT_USEHANDS|MT_EQUIP
	dam=1,8
	armor=15
	resources=8 i_ribs_raw
	FOODTYPE=15 t_meat_raw
	DESIRES=i_gold,spk_orc
	SHELTER=r_caves,r_dungeon,r_orc_camp
	AVERSIONS=r_civilization
	TSPEECH=spk_orc
	
	CATEGORY=UO:3D & UO:LBR
	SUBSECTION=Orcs
	DESCRIPTION=Orcish Bomber

	def create: #self is char
		NPC='brain_monster'
		STR={147 215}
		DEX={91 115}
		INT={61 85}

		PARRYING={60.0 85.0}
		MAGICRESISTANCE={70.0 85.0}
		TACTICS={75.0 90.0}
		WRESTLING={60.0 85.0}
		SWORDSMANSHIP={60.0 85.0}

		FAME={100 499}
		KARMA={-2000 -2999}

	def death: #src is char
		var.deathact=act.uid
		newitem('loot_orc_bomber')
		act.bounce()
		# Create death explosion to damage those nearby.
		f_explode(p)
		act=var.deathact
	#argo is the corpse's uid
	def deathcorpse: #src is char
		say("argo "+argo.uid)

#This is used by the orc bomber script.
def f_explode(pos):
	newitem('i_potion_explosionGreat')
	act.attr=attr_invis
	act.p=local.pos
	act.link=var.deathact
	act.more2=0320
	act.morex=1
	act.timer=1

#This was converted from a sample script PMouse posted on the sphereserver forums.
typedef t_MagicWeap_Prefix_Range_Accurate:
	def equip:
		src.archery=src.archery+46
		src.TACTICS=src.tactics+50
	def unequip:
		src.archery=src.archery-46
		src.TACTICS=src.tactics-50

#This was converted from a sample script PMouse posted on the sphereserver forums.
typedef t_MagicWeap_Suffix_theFox:
	def equip:
		src.maxhits=src.maxhits+3
	def unequip:
		src.maxhits=src.maxhits-3

#This was converted from a sample script PMouse posted on the sphereserver forums.
def f_MagicWeap_Prefix_Accurate():
	name="Accurate "+name
	events('+t_MagicWeap_Prefix_Range_Accurate')
	return(1)

#This was converted from a sample script PMouse posted on the sphereserver forums.
def f_MagicWeap_Suffix_theFox:
	name=name+" of The Fox" 
	events('+t_MagicWeap_Suffix_theFox')
	return(1)

#This was made to test both the of the preceding types at once.
def f_test_accurate_fox:
	f_MagicWeap_Prefix_Accurate()
	f_MagicWeap_Suffix_theFox()

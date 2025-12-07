#prefix-local
#omit-original-code

def Admin2:
	dialog('d_admin_system_2')

dialog d_admin_system_2(argo.tag.sortby, argo.tag.startindex):
	argo.PlayerList(argo.tag.sortby)	# fill list with clients.
	if not safe.argo.contextcount:
		src.sysmessage('No clients to list')
		return(1)
	SetLocation=5,80				# ok*
	page=0							# page 1*
	resizepic(0,0,5054,800,517)			# window*
	gumppictiled( 10, 10,780, 22,2624)	# title bar*
	gumppictiled( 10, 37,140,450,2624)	# navigation panel*
	gumppictiled(155, 37,615,450,2624)	# main panel
	gumppictiled( 10,490,780, 25,2624)	# status panel*
	checkertrans( 10, 10,780,507)		# make window transparent

	textA(30,12,2301,'"'+serv.name+' ADMIN CONSOLE -"')			# Main Title bar text
	textA(345,12,2301,'"'+"Client's Online Console ("+argo.contextcount+')"')
	button(760,10,4017,4019,1,0,0)		# exit button*

	textA(22,35,2301,'"goto"')
	textA(22+30,35,2301,'"jail"')
	textA(22+60,35,2301,'"msg"')				#MESSAGE
	textA(22+90,35,2301,'"admin"')				#ADMIN

	button(600,495,04b9,04ba,1,0,1)				# sort Account
	textA(160,35,2301,"Account")				# Account Name
	button(200,495,04b9,04ba,1,0,2)				# sort Name
	textA(280,35,2301,"Char")					# Char Name
	button(400,495,04b9,04ba,1,0,3)				# sort IPAddr
	textA(430,35,2301,"IP")						# IPAddr
	textA(540,35,2301,"Location")				# Location Title

	local.icontextcount=argo.contextcount
	#local.icount=0
	local.iqty=local.icontextcount-safe.argo.tag.startindex
	if local.iqty>100:
		local.iqty=100
	
	#src.smsg "begin index <?argo.tag.startindex?>, <?arg(iqty)?>"

	for local.icount in range(0,local.iqty):
	#while local.iqty>local.icount:
	#Thats local.icount<local.iqty
		
		if (local.icount%20)==0:
			local.iy=70
			local.ipage=1+(local.icount/20)
			argo.page(local.ipage)
			if local.icount:
				argo.button(700,460,0fa,0fb,0,local.ipage-1) # prev
			elif argo.tag.startindex:
				argo.button(700,460,0fa,0fb,1,0,4) 			# prev 100
			
			if (local.iqty>local.icount+20):
				argo.button(750,460,0fc,0fd,0,local.ipage+1) # next
			elif local.icontextcount-safe.argo.tag.startindex>100:
				argo.button(750,460,0fc,0fd,1,0,5) 			# next
			
		# Name, Val
		local.pClient=argo.ContextEnum(argo.tag.startindex+local.icount)

		argo.button(20,local.iy,4005,4007,1,0,(4*local.icount)+6) 		# goto
		argo.button(20+30,local.iy,4005,4007,1,0,(4*local.icount)+7) 	# jail
		argo.button(20+60,local.iy,4005,4007,1,0,(4*local.icount)+8) 	# msg
		argo.button(20+90,local.iy,4005,4007,1,0,(4*local.icount)+9) 	# admin

		argo.textA(160,local.iy,99,'"'+local.pClient.AccountName+'"')
		argo.textA(280,local.iy,99,'"'+local.pClient.Name+'"')
		argo.textA(430,local.iy,99,'"'+local.pClient.IPAddr+'"')
		argo.textA(540,local.iy,99,'"'+local.pClient.P+'"') 			# 440 last line to be made before next page

		local.iy+=20
		#local.icount+=1
	

dialogbutton d_admin_system_2:
	def 0:
		return
	def 1:
		src.dialog(d_admin_system2('"Account"',argo.tag.startindex))
	def 2:
		src.dialog(d_admin_system2('"Name"',argo.tag.startindex))
	def 3:	# Sort by
		src.dialog(d_admin_system2('"IPAddr"',argo.tag.startindex))
	def 4:	# page back 100
		src.dialog(d_admin_system2(argo.tag.sortby,(argo.tag.startindex-100)))
	def 5:	# page forward 100
		#src.smsg "page forward <?eval((argo.tag.startindex)+100)?>"
		src.dialog(d_admin_system2,'"'+argo.tag.sortby+'"',(argo.tag.startindex+100))

	def AnyButton:
		if (((argn-6)%4)==0):
			src.gouid(argo.contextEnum((argn-6)/4).uid)
		if (((argn-6)%4)==1):
			argo.contextEnum((argn-6)/4).jail
		if (((argn-6)%4)==2):
			src.targ=argo.contextEnum((argn-6)/4)
			src.everbtarg(hear)
		if (((argn-6)%4)==3):
			argo.tag.propback=1
			argo.tag.propback2='d_AdminPlayers'
			argo.contextEnum((argn-6)/4).tweak

#not yet implemented

contextmenu Menu_Context_Pet('Pet Menu'):
	def 0 (6107 020 0ff 0ff):
		Act=src.uid
		Hear('"Guard Me"')
	def 0 (6108):
		Act=src.uid
		Hear('"Follow Me"')
	def 0 (6109):
		Act=src.uid
		Hear('"Drop All"')
	def 0 (6111):
		Act=src.uid
		Hear('"Kill"')
	def 0 (6112):
		Act=src.uid
		Hear('"Stay"')
	def 0 (6106):
		Act=src.uid
		Hear('"Go"')
	def 0 (6110):
		Act=src.uid
		Hear('"Friend"')
	def 0 (6113):
		Act=src.uid
		Hear('"Transfer"')
	def 0 (6118):
		Act=src.uid
		Hear('"Release"')

menu MENU_TOWN_MAYOR_2('Town of '+Name+' ('+MasterTitle+' '+Master+')'):
	def 0 ('View the current citizenship.'):
		VIEWROSTER
	def 0 ("View the town's charter."):
		VIEWCHARTER
	def 0 ("Vote for mayor. You are currently loyal to "+LoyalTo+"."):
		DECLAREFEALTY
	def 0 ("Resign from the town."):
		RESIGN
	#def 0 ("View list of those banished from the town."):
	#	VIEWBANISHED
	def 0 ("View list of those applying for citizenship."):
		VIEWCANDIDATES
	def 0 ("View list of towns that "+Name" has declared war on."):
		VIEWENEMYS
	def 0 ("View list of towns that have declared war on "+Name+"."):
		VIEWTHREATS
	def 0 ("Access Mayoral functions."):
		MASTERMENU

#menudialog d_menu_town_mayor():
#	def main:
#		addText('Town of '+Name+' ('+MasterTitle+' '+Master+')')
#		addEntry('View the current citizenship.',0)
#		addEntry("View the town's charter.",1)
#		addEntry("Vote for mayor. You are currently loyal to "+LoyalTo+".",2)
#		addEntry("Resign from the town.",3)
#		addEntry("View list of those applying for citizenship.",4)
#		addEntry("View list of towns that "+Name" has declared war on.",5)
#		addEntry("View list of towns that have declared war on "+Name+".",6)
#		addEntry("Access Mayoral functions.",7)
#	def AnyButton:
#		if argn==0:
#			VIEWROSTER
#		elif argn==1:
#			VIEWCHARTER
#		elif argn==2:
#			DECLAREFEALTY
#		elif argn==3:
#			RESIGN
#		elif argn==4:
#			VIEWCANDIDATES
#		elif argn==5:
#			VIEWENEMYS
#		elif argn==6:
#			VIEWTHREATS
#		elif argn==7:
#			MASTERMENU
#			

menudialog d_menu_town_mayor_2():
	def main:
		addText('Town of '+Name+' (asdf)')
		addEntry('View the current citizenship.','VIEWROSTER')
		addEntry("View the town's charter.",'VIEWCHARTER')
		addEntry("Vote for mayor. You are currently loyal to yourself.",'DECLAREFEALTY')
		addEntry("Resign from the town.",'RESIGN')
		addEntry("View list of those applying for citizenship.",'VIEWCANDIDATES')
		addEntry("View list of towns that "+Name" has declared war on.",'VIEWENEMYS')
		addEntry("View list of towns that have declared war on "+Name+".",'VIEWTHREATS')
		addEntry("say moo.",'say','moo')
		addEntry("say my name.",'say',name)
		addText("The following text is space-filler to go to another page...")
		textColor(90)
		addText("b.")
		addText("c.")
		addText("d.")
		addText("e.")
		addText("f.")
		addText("g.")
		addText("h.")
		addText("i.")
		addText("j.")
		addText("k.")
		addText("l.")
		addText("m.")
		addText("n.")
		addText("o.")
		addText("p.")
		addText("q.")
		addText("r.")
		addText("s.")
		addEntry("set my name to bob.",'name','bob')

#You can also do AddEntry("Test",'f_my_func',uid,color), and if the button for "Test" is clicked, f_my_func will be called
#with parameters composed of whatever values uid and color had at the time the entry was added.


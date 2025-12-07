#prefix-local

#This uses the prefix-local notation (see the above comment - that indicates that it's what this file is using).
#It's pretty easy to see what prefix-local is from looking at this file and comparing it to prefix_sphere.py, which
#uses prefix-sphere notation instead.

#The #self is char lines indicate to the compiler what to call tryp on if compiling to 55i.

#testing spaces around equals signs in assignment commands, and also dynamic linking
def testspaces():		#self is char
	local.tempida=findlayer(21).uid
	local.tempidb = 0fca
	local.tempidc =0fca
	local.tempidd= uid
	say("Your backpack's name is "+local.tempida.name)
	local.tdef=local.tempidd.region.uid
	local.tdef.show('more2')
	#enable-replace
	finduid(0fca).show('name')
	#disable-replace
#This tests parameter passing in 55i.
def testParamPassing():		#self is char
	testarr(  5 , 9 , 73 , 99   )

#This tests arrays
def testarr(i, a):		#self is char
	tag.array[local.i]=5
	sysmessage("array["+local.i+"]="+tag.array[local.i])
	sysmessage("array["+local.i+"]="+tag.array[local.i]+".")

#This tests if, elif, and else.
def testif():		#self is char
	local.color=083ea
	if color==local.color:
		say("Yep, you're the standard color")
		if oskin==color:
			say("Your old skin is the same color, too.")
		else:
			say("Your old skin is a different color!")
	elif oskin==local.color:
		say("Your old skin is the standard color")
	elif color>local.color:
		say("You're above the standard color!")
	elif color<local.color:
		say("You're below the standard color!")
	else:
		say("You're the wrong color.")

#This tests the while loop.
def testwhile():	#self is char
	local.i=0
	while (local.i<5):
		say(local.i)
		local.i+=1

#This and testfor() tests for loops.
def testfor2():		#self is char
	for local.i in range(0,10):
		sysmessage("i "+local.i)
		tag.array[local.i]=local.i*local.i
	for local.ib in range(5,8):
		sysmessage("ib "+local.ib)
	for local.u in tag.array:
		sysmessage("u "+local.u)
def testfor():		#self is char
	for local.i in range(0,10):
		sysmessage("i "+local.i)
		tag.array[local.i]=local.i * local.i
		
	for local.ib in range(5,8):
		sysmessage("ib "+local.ib)
		
	for local.u in tag.array:
		sysmessage("u "+local.u)
		
	for local.iia in range(7,73,5):
		sysmessage("iia "+local.iia)
		
	for local.iib in range(8,3,-1):
		sysmessage("iib "+local.iib)

#This one uses eval. 
def testeval():		#self is char
	for local.i in range(0,10):
		tag.array[local.i]=eval(local.i*local.i)

#The eval statement doesn't come out right in this one, because of the space between it and the (.
#This is important. You can't have spaces between function names and their (.
def badeval():		#self is char
	for local.i in range(0,10):
		tag.array[local.i]=eval (local.i*local.i)
	
#try .lgimmeitem(i_reag_garlic)

#This creates the item the user specifies, and bounces it to their pack. Note that in the function argument, the "local."
#is not needed.
def lgimmeitem(itemID='i_reag_ginseng'):		#self is char
	newitem(local.itemID)
	act.bounce()

#This creates the item and bounces it, and uses the custom-linking code to do it. In 99u, the bounce uses finduid, and
#local.item holds a UID. In 55i, this will use act or link, depending on whether the caller is an item or char.
def lgimmeitem2(local.itemID='i_reag_garlic'):		#self is char
	local.item=newitem(local.itemID)
	local.item.color=021
	local.item.bounce()
	
#This tests some simple strings. Note the last line. Any string with commas in it will be compiled with actual qutoes
#around it in the outputted spherescript. Lines without commas won't, since the quotes interfere with things like you
#see in the 5th through 9th sysmessages in this function.
def lteststrings(local.num, local.text):		#self is char
	test=5
	sysmessage("Forsooth!")
	sysmessage('Forsay!eth')
	sysmessage('Testingeth')
	sysmessage("Aaaasdfdff")
	sysmessage("Your name is '"+name+"'")
	sysmessage('adding '+"'"+" '"+local.text+"'")
	sysmessage("single quote in double quote ' "+"'"+local.text+"'")
	sysmessage("no quotes "+local.text)
	sysmessage('using backslashes \' \''+local.text+'\'')
	sysmessage('This here line has some, well, commas in it.')
#sphere-55i
#prefix-sphere

#This contains some stuff that's also in prefix_local.py, except with an s instead of an l at the start of the function
#name. This file is just to demonstrate the prefix-sphere notation, so you can decide whether to use that or
#prefix-local.

#This file also tests UID references when compiling to 55i.

def sgimmeitem(itemID):
	sphere.newitem(itemID)
	sphere.act.bounce()

def sgimmeitem2(itemID):
	item=sphere.newitem(itemID)
	item.bounce()
	item.color(5)
	sphere.finduid(item).say("Moo.")

def steststrings(num, text):
	test=5
	sphere.echo(num)
	sphere.sysmessage("Forsooth!")
	sphere.sysmessage('Forsay!eth')
	sphere.sysmessage('Testingeth')
	sphere.sysmessage("Aaaasdfdff")
	sphere.sysmessage("Your name is '"+sphere.name+"'")
	sphere.sysmessage('sayin'+"'"+" '"+text+"'")
	sphere.sysmessage("sayin' "+"'"+text+"'")
	sphere.sysmessage("sayin' "+text)
	sphere.sysmessage('sayin\' \''+text+'\'')

#prefix-local

#exclude-quotes
#the preceding is needed to make PySphere not automatically insert ""s around a string with a comma in it.

def stringtest():
	say('"abcdef')
	say('"abcdef '+name)
	say('"abcdef '+name+' moo')
	say('"abcdef '+name+' moo"')
	say('"You need '+local.mC+' mana of the appropriate type, and have only '+tag.mana[local.pMT]+'."')
		
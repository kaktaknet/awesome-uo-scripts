#Omitting the sphere ver specifier makes it use the most recent supported sphere version, as of 99w.
#prefix-local

#This little file tests only one thing. The showargs() function actually prints out every argument passed to the function,
#Note that if one of the args is an empty string, none of the args after it will be noticed. This is a consequence
#of the way 'for' was coded for arrays.

#Also, note that you CAN NOT use this sort of for loop on a string to get each character. Nor can you use Python's
#mystring[2:5] notation to get parts of a string. Not yet, anyhow. You'll have to use strmid, etc.

def showargs():
	for local.v in argv:
		sysmessage("arg "+local.v__val+" is "+local.v)

		
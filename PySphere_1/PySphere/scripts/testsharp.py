#prefix-local

def testsharp:
	local.i=0
	local.i+=42
	local.i-=17
	local.i*=53
	local.j=local.i
	local.j%=22
	local.i/=22
	var.x*=5
	
	sysmessage('local.i='+local.i+'. It should be 60.')
	sysmessage('local.j='+local.j+'. It should be 5.')

#sphere-99w
def testnosharp:
	local.i=0
	local.i+=42
	local.i-=17
	local.i*=53
	local.j=local.i
	local.j%=22
	local.i/=22
	var.x*=5
	
	sysmessage('local.i='+local.i+'. It should be 60.')
	sysmessage('local.j='+local.j+'. It should be 5.')

#produce-readable-code
#sphere-99x
def testreadsharp:
	local.i=0
	local.i+=42
	local.i-=17
	local.i*=53
	local.j=local.i
	local.j%=22
	local.i/=22
	var.x*=5
	
	sysmessage('local.i='+local.i+'. It should be 60.')
	sysmessage('local.j='+local.j+'. It should be 5.')

#sphere-99w
def testreadnosharp:
	local.i=0
	local.i+=42
	local.i-=17
	local.i*=53
	local.j=local.i
	local.j%=22
	local.i/=22
	var.x*=5
	
	sysmessage('local.i='+local.i+'. It should be 60.')
	sysmessage('local.j='+local.j+'. It should be 5.')

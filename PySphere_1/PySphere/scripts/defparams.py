#prefix-local

#This tests default parameters

def testParamPassing2():
	test_defparams(  5 , 9 , 73 , 99   )
	test_defparams(1)

def test_defparams(i=10, a=20):
	sysmessage("i="+local.i)
	sysmessage("a="+local.a)

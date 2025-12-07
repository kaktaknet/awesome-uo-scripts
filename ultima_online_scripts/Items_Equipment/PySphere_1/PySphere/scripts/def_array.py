#prefix-local
#omit-original-code

#Either defnames or defname works here
defnames def_test_array:
	#You don't have to do anything special to indicate that test_array is an array defname except using []s.
	#You can use strings instead of numbers as the array index, if you want.
	test_array[0]='qwer'
	test_array[1]='asdf'
	test_array[2]='zxcv'
	test_array[3]='tyuiop'
	test_array[4]='ghjkl'
	test_array[5]='bnm'
	#These two are not necessary, but I use them.
	test_array_min=0
	test_array_max=5
	
def f_test_def_array(local.num):
	#Checking to make sure it's a valid array index
	if local.num>test_array_min and local.num<test_array_max:
		#Just like accessing a regular array.
		local.val=test_array[local.num]
		say('That one is '+local.val)
	else:
		say('You should pass a number between '+test_array_min+' and '+test_array_max+'.')

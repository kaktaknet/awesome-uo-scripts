#prefix-local
#omit-original-code

def f_foo(x,y):
	if x>0:
		if y>0:
			say('y>0')
		else:
			say('y<=0')
		say('x>0')
	else:
		say ('x<=0')
	say ('moo')

def f_bar(x,y):
	if x>0:
		say('x>0')
		if y>0:
			say('y>0')
		elif y<0:
			say('y<0')
		else:
			say('y=0')
		say('x>0 again')
	else:
		say('x<=0')
		if y>0:
			say('y>0')
		elif y<0:
			say('y<0')
		else:
			say('y=0')
		say('x<=0 again')
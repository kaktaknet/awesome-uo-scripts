#produce-readable-code
#sphere-99w
#prefix-local
#omit-original-code

#This tests several things. Note that this compiles to 99w. If it compiled to 99v, the first for would use argvlen,
#but the second one would not work anymore unless you set tag.testarrLEN. As 99w, it displays indices 0-3, but not 5,
#since 4 registers as ''.

def f_argv_test():
	for local.arg in argv:
		say('arg # '+local.arg__val+' is '+local.arg)
	tag.testarr[0]='asdf'
	tag.testarr[1]='zxcv'
	tag.testarr[2]='qwerxx'
	tag.testarr[3]='dfgha'
	tag.testarr[4]=
	tag.testarr[5]='zzz'
	for local.arg in tag.testarr:
		say('arg # '+local.arg__val+' is '+local.arg)
	newitem('i_pickaxe')
	act.bounce()
	say('act is '+act)
	say('src.act is '+src.act)
	say('act.uid is '+act.uid)
	say('src.act.uid is '+src.act.uid)
	newitem('i_gold')
	act.bounce()
	act.say('act saying name is '+name)
	act.say('act saying act.name is '+act.name)
	act.say('act saying this.name is '+this.name)
	act.say('act saying i.name is '+i.name)
	
def f_test_tart():
	newitem('i_bag')
	act.cont('uid') 
	newitem('i_gold')
	act.cont('i.uid') 

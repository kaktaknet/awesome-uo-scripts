#prefix-local
#omit-original-code

def f_doswitch_test(local.x):
	if (local.x<1) or (local.x>12):
		say('Pass a number from 1 to 12.')
		return
	else:
		local.monthname='Unknown'
		doswitch local.x:
			local.monthname='None'
			local.monthname='January'
			local.monthname='February'
			local.monthname='March'
			local.monthname='April'
			local.monthname='May'
			local.monthname='June'
			local.monthname='July'
			local.monthname='August'
			local.monthname='September'
			local.monthname='October'
			local.monthname='November'
			local.monthname='December'
		say('Month '+local.x+' is '+local.monthname)

def f_dorand_test():
	dorand 5:
		say('First random choice.')
		say('Second random choice.')
		say('Third random choice.')
		say('Fourth random choice.')
		say('Fifth random choice.')

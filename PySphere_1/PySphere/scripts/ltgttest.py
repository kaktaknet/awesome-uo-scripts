def f_test_link_ltgt():
	#Expects to be called on an item which has tag.onsuccess set to the name of a function, and tag.args set.
	if link.color<255:
		link.<tag.onsuccess>(tag.args)
	if link.color>255:
		pass
	if <link.color><255:
		pass
	if <link.color>>255:
		pass
	
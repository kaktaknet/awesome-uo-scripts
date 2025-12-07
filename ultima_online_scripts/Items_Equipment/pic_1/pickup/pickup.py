
# A double clicked item will be bounced into the backpack
# Useful for arrows/bolts

import wolfpack

def onUse( char, item ):
	if item.container:
		return False

	if char.canreach( item, 3 ):
		if not wolfpack.utilities.tobackpack(item, char):
			item.update()
		char.socket.sysmessage( "You pick up the item." )
	else:
		char.socket.clilocmessage( 500312 ) # You cannot reach that.
	return True

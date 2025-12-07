#===============================================================#
#  WOLFPACK 13.0.0 Scripts
#  Created by: Naddel
#  Feel free to do with this whatever you want
#===============================================================#

import wolfpack
import wolfpack.console

#
# A scripted systemmessage function
#
def systemmessage( arguments, color=55 ):
	socket = wolfpack.sockets.first() 
	while socket:
		if socket.player:
			socket.sysmessage("%s" % arguments, color)
		socket = wolfpack.sockets.next()


"""
	\command shutdown
	\usage - <code>shutdown <time>,<reason></code>
	- <code>shutdown immediately</code>
	\description Shows a sysmessage to all connected players with the reason of the shutdown and a 
	kind of countdown (every minute). ".shutdown immediately" shuts the server immediately.
"""
def shutdown(socket, command, arguments):
	args = arguments.strip()
	args = args.split( ",", 1 )
	if len(args) == 1:
		if arguments == "immediately":
			wolfpack.queueaction( SAVE_WORLD )
			wolfpack.console.shutdown()
		else:
			socket.sysmessage( "Usage: shutdown <time in minutes>, <reason>" )
		return True
	( time, reason ) = args
	try:
		int(time)
	except:
		socket.sysmessage( "Time must be a number!" )
		return True
	if time < 1:
		socket.sysmessage( "Usage: shutdown <time in minutes>, <reason>" )
		return True
		
	wolfpack.addtimer( 1000 * 0, "commands.commands.shutdown_timer", [time, socket, reason] )

def shutdown_timer( char, args ):
	time = args[0]
	char = args[1]
	reason = args[2]
	if time < 0:
		return True
	if zeit == 0:
		wolfpack.queueaction( SAVE_WORLD )
		wolfpack.console.shutdown()
		return True
	systemmessage( "Server is shutting down in %s minutes: %s" % (time, reason) )
	zeit = int(zeit) - 1
	wolfpack.addtimer( 1000 * 60, "commands.commands.shutdown_timer", [time, char, reason] )


"""
	\command broadcast
	\usage - <code>broadcast <message></code>
	- <code>broadcast <color>, <message></code>
	\description Broadcast a message to all connected clients.
	Message is the message you want to broadcast to everyone, color is the color of the message
	(can be any numbers (max. 4), have fun playing ;)).
"""
def broadcast(socket, command, args):
	args = args.strip()
	if len(args) == 0:
		socket.sysmessage( "Usage: broadcast <color>, <message>" )

	args = args.split( ",",1 )
	
	if len( args ) > 0:
		if len(args) == 1:
			( message ) = args[0]
			systemmessage( message )
		if len(args) > 1:
			try:
				( col, message ) = args
				farbe = int(col)
				if len(col) > 4: # otherwise Client Crash!
					socket.sysmessage( "Color can be only 4 numbers!" )
					return True
				systemmessage( message, farbe )
			except:
				systemmessage( "%s, %s" % (args[0], args[1]) )
		return True

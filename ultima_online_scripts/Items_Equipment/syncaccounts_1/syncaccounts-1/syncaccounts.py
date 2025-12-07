#
# This script synchronizes account information from a mysql database
# with the account database used by the wolfpack server.
#

import wolfpack
from wolfpack.consts import *
from wolfpack import console, accounts
import random
from threading import Thread, Event, Lock
import MySQLdb
import time

# Configuration
interval = float(120) # In Seconds (2 minutes)

scriptname = 'syncaccounts'

# MySQL Settings
mysql_host = 'localhost'
mysql_user = 'root'
mysql_pass = ''
mysql_db = 'wolfpack'

# Dont change
processthread = None

# 0, 1, 2, 3, 4, 5, 6, 7
ACLS = ['player', 'player', 'counselor', 'seer', 'gm', 'admin', 'admin', 'admin']

#
# This thread processes the data from the database
# and puts it into a format readable by the server.
#
class ProcessThread(Thread):
	# Initialize this thread
	def __init__(self):
		Thread.__init__(self)
		self.stopped = Event() # Cancel Event
		self.mutex = Lock()
		self.processed = True # Start as True
	
	# This code runs in a separate thread
	def run(self):
		global interval

		while not self.stopped.isSet():
			# Get the processing state
			self.mutex.acquire()
			processed = self.processed
			self.mutex.release()
			
			# Only gather new data if the old has been processed
			if processed and wolfpack.isrunning():
				# Retrieve data from the database and put it into a format
				# readable by the timer.
				data = []
				
				# Connect to the database
				try:
					connection = MySQLdb.connect(db=mysql_db,user=mysql_user,passwd=mysql_pass,host=mysql_host)				
					cursor = connection.cursor() # Acquire a database cursor
					
					# Execute the query.
					cursor.execute("SELECT username,password,blocked,plevel FROM ar_user WHERE pending = 0;")
					
					# Get all results
					result = cursor.fetchone()
					while result:
						(username, password, blocked, plevel) = result
						username = username.decode('latin').lower()
						data.append( (username, password, blocked, plevel) ) # Store the resultset
						result = cursor.fetchone()
	
					cursor.close() # Free the cursor
					
					connection.close() # Free the database connection
				except Exception, e:
					console.log(LOG_ERROR, 'An error occured while synchronizing the accounts:\n%s\n' % str(e))
					data = None
	
				# If there is no result, it's highly likely there has
				# been an error.
				if data and len(data) != 0:
					# Queue the synchronization to be done with the next mainthread iteration
					if wolfpack.isrunning():
						self.processed = False
						wolfpack.queuecode(autosyncaccounts, (data,))

			# Wait until canceled or the next interval
			self.stopped.wait(interval)
			
#
# A wrapper for the autosyncaccounts function used in
# wolfpack timers.
#
def autosyncaccountswrapper(object, args):
	autosyncaccounts(args[0], args[1])	

#
# Automatically sync the thread data with the normal data once
# every minute.
#
def autosyncaccounts(data, stage = 0):
	global processthread
	
	# Only process data if there is any
	starttime = time.time()
	
	added = 0
	removed = 0
	
	if stage == 0:
		names = accounts.list()
		namehashes = []
	
		for name in names:
			namehashes.append(hash(name))
			
		hashes = []
		for result in data:
			hashes.append(hash(result[0]))
			
		# Check for removed accounts first
		for i in range(0, len(names)):
			namehash = namehashes[i]
			name = names[i]
			
			# Find a new username with the same hash
			found = namehash in hashes
									
			# Remove the account
			if not found:
				account = accounts.find(name)
				if account:
					console.log(LOG_MESSAGE, 'Removing account %s.\n' % name)
					account.delete()
					removed += 1
			
		#wolfpack.queuecode(autosyncaccounts, (data, 1))
		# It's more useful to use a timer here since that will give the server
		# time to process networking events.
		wolfpack.addtimer(1000, scriptname + '.autosyncaccountswrapper', [data, 1])

	elif stage == 1:
		# Now check for new ones or update old ones
		for result in data:
			name = result[0]
			
			account = accounts.find(name)
						
			# Create
			if not account:
				added += 1
				account = accounts.add(name, '')
				if not account:
					console.log(LOG_ERROR, 'Error while adding account %s.\n' % result[0])
					continue
	
			# Set Password and E-Mail
			if account.rawpassword != result[1]:
				account.rawpassword = result[1]
			
			# Block / Unblock account
			if result[2]:
				if account.flags & 0x01 == 0:
					account.block()
					console.log(LOG_MESSAGE, 'Blocking account %s.\n' % result[0])
			else:
				if account.flags & 0x01 != 0:
					account.unblock()
					console.log(LOG_MESSAGE, 'Unblocking account %s.\n' % result[0])
			
			if result[3] > 7:
				acl = ACLS[7]
			else:
				acl = ACLS[result[3]]
				
			# This should save some time.
			if account.acl != acl:
				account.acl = acl
				
		# We finished processing the data
		processthread.mutex.acquire()
		processthread.processed = True
		processthread.mutex.release()

	# Calculate the time it took to process
	endtime = time.time()
	delay = (endtime - starttime) * 1000
	
	# Output a fitting message.
	if stage == 0:
		console.log(LOG_MESSAGE, "Synchronized %u accounts in %u ms. (Removed: %u)\n" % (len(data), delay, added))
	elif stage == 1:
		console.log(LOG_MESSAGE, "Synchronized %u accounts in %u ms. (Added: %u)\n" % (len(data), delay, added))

#
# Register a new command for forcing a data update.
#
def onLoad():	
	# Send a message to the log
	console.log(LOG_MESSAGE, "Starting account synchronization thread.\n")
	
	# Create the worker thread
	global processthread
	processthread = ProcessThread()
	processthread.start()

#
# Shutdown the thread
#	
def onUnload():	
	console.log(LOG_MESSAGE, "Stopping account synchronization thread.\n")

	global processthread
	if processthread:
		processthread.stopped.set()
		time.sleep(0.01) # Sleep a little to give the thread time to exit
		if processthread:
			processthread.join()
		processthread = None

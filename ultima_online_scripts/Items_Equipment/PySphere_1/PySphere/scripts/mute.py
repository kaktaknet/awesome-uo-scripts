#prefix-local
#omit-original-code

defnames def_allowed_commands:
	underwear 	1
	mute 		6
	ACCOUNTAGE	1
	AFK			1
	ANIM		1
	DETAIL		1
	SLEEP		1
	UNDERWEAR	1
	WHERE		1
	HUNGRY		1
	CAST		1
	TELE		1
	SUICIDE		1
	FLIP		1
	self		1
	LAST		1
	BARK		1
	HELP		1
	PASSWORD	1
	EMAIL		1
	HelpPage	1
	UNEQUIPALL	1

	RESEND		2
	SYNC		2
	RESYNC		2
	FIX			2
	INFO		2
	PROPS		2
	TWEAK		2
	CLIENTS		2
	ADMIN		2
	PAGE		2
	GO			2
	GOUID		2
	GOCHAR		2
	GOSOCK		2
	GOCLI		2
	XGO			2
	JAIL		2
	FORGIVE		2
	PARDON		2

	CHARLIST	3

	LINK		4
	TILE		4
	NUKE		4
	GOTYPE		4
	GONAME		4

	SAVE		5

	ACCOUNT		6
	SETPRIV		6
	DIALOG		6
	BLOCKIP		6
	TOME		6
	EXTRACT		6
	UNEXTRACT	6
	EXPORT		6
	import		6

def mute:
	if not safe.args:
		tag.mutemode=
		events('-e_mute')
	else:
		tag.mutemode=args
		events('+e_mute')
		everbtarg(finduid(uid).mute_sub)
	clear


def mute_sub:
	if not isevent('e_mute'):
		return(1)
	if (strmatch(.*,args)):
		if (safe.tag.mutemode<=1):
			if (account.plevel>=safe.var.<args>):
				try('finduid(<uid>)<args>')
	elif (safe.tag.mutemode==2):
		say(args)
	everbtarg(finduid(uid).mute_sub)
	clear

events e_mute:
	def login:
	everbtarg(finduid(uid).mute_sub)
	
def clear:
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
	SYSMESSAGE
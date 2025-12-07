#PySphere
#Copyright 2002-2003 Richard Dillingham

releaseNumber='17'
mostRecentSphereVer='99z'

enableDefNameChecking=1
enableScpDefNameChecking=0
enableTimeChecking=1
useScpDefNameList=1

from __future__ import division
import os, sys, os.path, string
import cPickle
import getpass
import telnetlib
import time
import socket
import Patterns

#First thing that's run. Well, second thing. The very last line of this file is the first thing, and it calls this.
def main():
	print "PySphere Release "+releaseNumber+" - Copyright 2002-2003 Richard Dillingham (Shadowlord)"
	os.chdir(os.path.join('..','scripts'))
	compiler = Compiler()
	compiler.knownFunctions=[]
	compiler.knownDefNames={}
	compiler.knownScpDefNames=[]
	preCompilePy(os.listdir("."), compiler)
	print "Searching scripts for defnames."
	if enableDefNameChecking:
		if useScpDefNameList:
			defs=os.path.join('..','defs.ini')
			enableScpDefNameChecking=0
			if os.path.exists(defs):
				deffile=open(defs,'r')
				line=deffile.readline()
				while (len(line)>0 and line[-1]=='\n'):
					compiler.addDefName(line[:-1])
					line=deffile.readline()
				deffile.close()
				
			else:
				print "Generating defs.ini. (This will only be done once.)"
				preLoadScpDefs(os.listdir("."), compiler)
				deffile=open(defs,'w')
				for a in compiler.knownScpDefNames:
					#print 'writing '+a
					deffile.write(a+'\n')
					compiler.addDefName(a)
				deffile.close()
		preLoadDefs(os.listdir("."), compiler)
	
	print "Checking for pysphere.cfg."
	resync=0
	host='127.0.0.1'
	port=2593
	account=''
	password=''
	cfgs=os.path.join('..','pysphere.ini')
	if os.path.exists(cfgs):
		cfgfile=open(cfgs,'r')
		line=cfgfile.readline()
		while (len(line)>0 and line[-1]=='\n'):
			lines=string.split(line,'=')
			if lines[0]=='host':
				host=lines[1].rstrip('\n')
			if lines[0]=='port':
				port=int(lines[1].rstrip('\n'))
			if lines[0]=='account':
				account=lines[1].rstrip('\n')
			if lines[0]=='password':
				password=lines[1].rstrip('\n')
			line=cfgfile.readline()
			
		cfgfile.close()
		if len(password)>0:
			resync=1
		
	else:
		print "Writing pysphere.ini."
		cfgfile=open(cfgs,'w')
		cfgfile.write('host=127.0.0.1\nport=2593\naccount=\npassword=\n')
		cfgfile.close()
	
	tn = telnetlib.Telnet()
	
	if resync:
		print "Connecting to Sphere."
		try:
			pos=0
			tn.open(host,port)
			pos=1
			tn.write(' ')
			time.sleep(0.1) #pause
			if len(account)>0:
				tn.write(account + "\n")	
			time.sleep(0.1) #pause
			tn.write(password + "\n")
			print "Starting resync."
			time.sleep(0.2) #pause
			tn.write('R\n')
		except socket.error:
			if pos==0:
				print "Sphere is not running, skipping resync. (This is not an error.)"
			else:
				print "Sphere rejected our login attempt."
			resync=0
		#connect to sphere and resync pause
		
	try :
		compilePy(os.listdir("."), compiler)
	finally :
		#always run this block of code, even if there's an error in the compiling.
		if resync:
			#resync resume
			print "Ending resync and disconnecting from Sphere."
			tn.write('R\n')
			time.sleep(0.2) #pause
			tn.close()
		
	print "Done!"
	
#Third thing that's run. Memorizes function names and parameters.
def preCompilePy(files, compiler):
	for file in files:
		if file[-3:]=='.py':
			compiler.preCompileFile(file)
		elif os.path.isdir(file):
			#print "Searching "+file
			os.chdir(file)
			preCompilePy(os.listdir("."), compiler)
			os.chdir("..")

#Fourth thing that's run. This takes a list of files, and reads definitions from all .scp's in it, and recurses into all folders.
def preLoadDefs(files, compiler):
			
		
	for file in files:
		if file[-4:]=='.scp' and enableScpDefNameChecking:
			compiler.searchFileForDefs(file, 1)
		elif file[-3:]=='.py':
			#print 'loading defs from '+file
			compiler.searchFileForDefs(file, 2)
		elif os.path.isdir(file):
		#	print "Searching "+file
			os.chdir(file)
			preLoadDefs(os.listdir("."), compiler)
			os.chdir("..")

#Preload defs from .scp files. This is called by the code which generates defs.ini.
def preLoadScpDefs(files, compiler):
	for file in files:
		if file[-4:]=='.scp':
			if not (os.path.exists(file[:-4]+'.py')):
				#print "Searching for defs in "+file
				compiler.searchFileForDefs(file, 1)
		elif os.path.isdir(file):
			#print "Searching "+file
			os.chdir(file)
			preLoadScpDefs(os.listdir("."), compiler)
			os.chdir("..")

		
#Fifth thing that's run. This takes a list of files, and compiles all .py's in it, and recurses into all folders.
def compilePy(files, compiler):
	for file in files:
		if file[-3:]=='.py':
			compiler.compileFile(file)
		elif os.path.isdir(file):
			#print "Searching "+file
			os.chdir(file)
			compilePy(os.listdir("."), compiler)
			os.chdir("..")

#The compiler class. I use self. stuff a lot with this.
class Compiler:
	def __init__(self):
		self.patterns={}
		self.supports={}
		self.convert={}
		self.scp=None
		Patterns.add99u(self)
		Patterns.add55i(self)
		Patterns.add99v(self)
		Patterns.add99w(self)
		Patterns.add99x(self)
		#VerA exists because both 99y and 99z use the same patterns.
		Patterns.addVerA(self,'99y')
		Patterns.addVerA(self,'99z')
		self.whatischar=''
	
	def searchFileForDefs(self, file, fileType):
		#print "Searching "+file+" for definitions."
		self.moduleName=file
		self.py=open(file,'r')
		eof=0
		self.lineNum=0
		self.blocks=[]
		self.blockTab=0
		self.inDefName=0
		
		while eof==0:
			line = self.py.readline()
			self.lineNum+=1
			if line[-1:]=='\n':
				line=line[:-1]
			else:
				eof=1
			self.searchLineForDefs(line, fileType)
		self.py.close()
		
	def searchLineForDefs(self,line, fileType):
		strline = line
		if fileType==1:
			commentPos = strline.find('//')
		else:
			commentPos = self.finds(strline,'#',0)
		if commentPos>-1:
			
			strline=strline[:commentPos]
		if len(strline)==0:
			return
		ft=0
		if fileType==1:
			defnamePos = strline.lower().find('[defname')
		else:
			defnamePos = strline.lower().find('defname')
		if defnamePos>-1:
			#print 'defname found: '+strline
			spacePos = strline.lower().find(' ',defnamePos)
			if spacePos>-1:
				if fileType==1:
					rbracketPos = strline.lower().find(']',spacePos)
				else:
					rbracketPos = strline.lower().find(':',spacePos)
				if rbracketPos>-1:
					#print 'defnames start'
					self.inDefName=1
				return
		else:
			if fileType>0:
				lbracketPos = strline.lower().find('[')
				if lbracketPos==0:
					self.inDefName=0
				else:
					if self.inDefName==1:
						#print strline
						spacePos = strline.lower().find(' ')
						tabPos = strline.lower().find('\t')
						eqPos = strline.lower().find('=')
						lbPos = strline.lower().find('[')
						pos=tabPos
						if pos==-1:
							pos=len(strline)
						if spacePos>-1 and spacePos<pos:
							pos=spacePos
						if eqPos>-1 and eqPos<pos:
							pos=eqPos
						if lbPos>-1 and lbPos<pos:
							pos=lbPos
						if pos==-1 or pos>=len(strline):
							return
						defName=strline.lower()[:pos]
						#print "def found: "+defName
						if fileType==2:
							self.addDefName(defName)
						elif fileType==1:
							self.addScpDefName(defName)
						return
					
			else:
				numTabs = self.countTabs(strline)			
				if numTabs==1 and self.inDefName==1:
					spacePos = strline.lower().find(' ',1)
					tabPos = strline.lower().find('\t',1)
					eqPos = strline.lower().find('=',1)
					lbPos = strline.lower().find('[',1)
					pos=tabPos
					if pos==-1:
						pos=len(strline)
					if spacePos>-1 and spacePos<pos:
						pos=spacePos
					if eqPos>-1 and eqPos<pos:
						pos=eqPos
					if lbPos>-1 and lbPos<pos:
						pos=lbPos
					if pos==-1 or pos>=len(strline):
						return
					defName=strline.lower()[:pos].strip()
					self.addDefName(defName)
					return
				elif numTabs!=1 and self.inDefName==1:
					self.inDefName=0
					return
			
	def preCompileFile(self, file):
		self.moduleName = file[:-3]
		scpFile = file[:-3]+'.scp'
		print "Parsing "+file+" for function definitions."
		self.py=open(file,'r')
		pyt=os.stat(file).st_mtime
		if os.path.exists(scpFile):
			scpt=os.stat(scpFile).st_mtime
		else:
			scpt=0
		if (enableTimeChecking and pyt>=scpt):
			scpFile = self.moduleName+'.pyc'
			scp=open(scpFile,'w')
			scp.write("//This file hasn't been compiled.\n")
			scp.close()
		self.prefixSphere=0
		self.prefixLocal=0
		self.prefixAuto=0
		self.sphereVer=mostRecentSphereVer
		self.excludeQuotes=0
		eof=0
		self.lineNum=0
		self.blocks=[]
		self.blockTab=0
		
		while eof==0:
			line = self.py.readline()
			self.lineNum+=1
			if line[-1:]=='\n':
				line=line[:-1]
			else:
				eof=1
			self.preparseline(line)
		self.preparseline('\t')
		self.py.close()
		
	def addDefName(self,defname):
		if (len(defname.strip())>0):
			if not self.isKnownDefName(defname):
				self.knownDefNames[defname.lower()]=1
			
	def addScpDefName(self,defname):
		if (len(defname.strip())>0):
			self.knownScpDefNames.append(defname.lower())
		
	
	def translateKnownArrayDefNames(self, strline):
		for defn in self.knownDefNames:
			s=strline.lower().find(defn.lower()+'[')
			while s>-1:
				print defn
				srb=strline.find(']',s)
				strline=strline[:s]+defn+'_'+strline[s+len(defn)+1:srb]+strline[srb+1:]
				s=strline.lower().find(defn.lower()+'[')
		return strline	
			
	def translateArrayDefName(self,defname):
		lbr = self.finds(defname,'[',0)
		while lbr>-1:
			defname = defname[:lbr]+'_'+defname[lbr+1:]
			lbr = self.finds(defname,'[',lbr)
			
		rbr = self.finds(defname,']',0)
		while rbr>-1:
			defname = defname[:rbr]+defname[rbr+1:]
			rbr = self.finds(defname,']',rbr)
		return defname
			
	def isKnownArrayDefName(self,defnameA):
		lbr = self.finds(defnameA,'[',0)
		defname=defnameA[:lbr].strip()
		try:
			if self.knownDefNames[defname.lower()]==1:
				return 1
		except KeyError:
			pass
		return 0
	
	def isKnownDefName(self,defname):
		try:
			if self.knownDefNames[defname.lower()]==1:
				return 1
		except KeyError:
			pass
		return 0
	
	def addPreProcessedFunction(self,functionName, args):
		self.knownFunctions.append((functionName.lower(),args))
		
	def isKnownFunction(self,functionName):
		for a in range(0,len(self.knownFunctions)):
			if self.knownFunctions[a][0]==functionName.lower():
				return a
		return -1
		
	def getArgs(self,function):
		if function.__class__==str:
			a=self.isKnownFunction(function)
			if a!=-1:
				return self.knownFunctions[a][1]
		else:
			return self.knownFunctions[function][1]
		return []
		
	def preparseline(self,line):
		strline = line
		commentPos = self.finds(strline,'#',0)
		if commentPos>-1:
			if strline.lower()=="#prefix-sphere":
				self.prefixSphere=1
			elif strline.lower()=="#prefix-local":
				self.prefixLocal=1
			elif strline.lower()=="#prefix-auto":
				self.prefixAuto=1
			if strline.lower()=="#exclude-quotes":
				self.excludeQuotes=1
			if len(strline)>8 and strline[:8].lower()=="#sphere-":
				self.sphereVer=strline[8:]
			strline=strline[:commentPos]
			if len(strline)==0:
				return ""
		numTabs = self.countTabs(strline)
		if len(strline)>3:
			if strline[:3].lower()=='def':
				#function definition. Not tabbed, so NOT a trigger definition
				self.functionName = strline[3:].strip()
				args = None
				paren = self.functionName.find('(')
				colon = self.functionName.find(':')
				if paren>-1:
					paren2 = self.findn(self.functionName,')',paren)
					argtxt = self.functionName[paren+1:paren2]
					args = self.split(argtxt,',')
					self.functionName=self.functionName[:paren]
				else:
					if colon>-1:
						self.functionName=self.functionName[:colon]
				if args!=None:
					num=0
					for arg in range(0,len(args)):
						if self.prefixLocal==1 and args[arg].strip().lower().find('local.')==0:
							args[arg]=args[arg].strip()[6:]
						num+=1
				self.addPreProcessedFunction(self.functionName, args)
				return
		
	#Compile one particular file.
	def compileFile(self, file):
		pycFile = file[:-3]+'.pyc'
		scpFile = file[:-3]+'.scp'
		pyt=os.stat(file).st_mtime
		if os.path.exists(scpFile):
			scpt=os.stat(scpFile).st_mtime
		else:
			scpt=0
		if (enableTimeChecking and pyt<scpt):
			return
		self.moduleName = file[:-3]
		print "Compiling "+file+" to "+scpFile
		self.py=open(file,'r')
		self.scp=open(pycFile,'w')
		self.scp.write('//'+scpFile+' compiled by PySphere Release '+releaseNumber+' from '+file+'.\n')
		self.enableReplacer=1
		self.produceReadableCode=0
		self.includeOriginalCode=1
		self.prefixSphere=0
		self.prefixLocal=0
		self.prefixAuto=0
		self.sphereVer=mostRecentSphereVer
		self.excludeQuotes=0
		self.extraText=[]
		self.writeToExtraText=0
		self.inScriptDef=0
		eof=0
		self.lineNum=0
		self.blocks=[]
		self.extraTextBlocks=[]
		self.blockTab=0
		if self.supports[self.sphereVer]['<??>']:
			self.evalStartChar='<?'
			self.evalEndChar='?>'
		else:
			self.evalStartChar='<'
			self.evalEndChar='>'
		
		while eof==0:
			line = self.py.readline()
			self.lineNum+=1
			if line[-1:]=='\n':
				line=line[:-1]
			else:
				eof=1
			self.parseline(line)
		self.parseline('\t')
		while self.blockTab>0:
			st = self.blocks.pop()
			if st!=None:
				self.scp_write(st)
			st = self.extraTextBlocks.pop()
			if st[0]!=None:
				self.extraText.append(st[0])
			if st[1]==1:
				self.writeToExtraText=0
			self.blockTab-=1
		for t in self.extraText:
			self.scp.write(t)
		self.py.close()
		self.scp.close()
		if os.path.exists(scpFile):
			os.remove(scpFile)
		os.rename(pycFile,scpFile)
	
	def doReplaceAll(self,arg):
		if self.enableReplacer:
			changes = self.convert[self.sphereVer]
			for frmto in changes:
				arg=self.replace(arg,frmto[0],frmto[1])
		return arg
		
	def scp_write(self,arg):
		if arg.lower()=='pass\n':
			return
		arg=self.doReplaceAll(arg)
		if self.sphereVer=='55i':
			newi = arg.find('newitem')
			lt = arg.find('<')
			gt = arg.find('>')
			eq = arg.find('=')
			lp = arg.find('(')
			eqq = arg.find('==')
			ifp = arg.lower().find('if')
			if eq!=-1 and newi!=-1 and eq<lt<newi:
				onwho=arg[:eq]
				tempactvname='var.py__'+self.moduleName+'__'+self.functionName+'__tempact'
				runner=arg[eq+1:newi]
				arg=tempactvname+'='+runner+'act.uid>\n'+self.stripLTGT(arg[eq+1:].strip())+'\n'+onwho+'=<act.uid>\n'+self.stripLTGT(runner)+'act=<'+tempactvname+'>\n'
			elif (eq==-1 and eqq==-1 and ifp==-1 and lt<gt) or (lt<gt<eq and eqq!=eq and ifp==-1):
				if lp==-1 or (lp>-1 and lt<gt<lp):
					arg=self.whatischar+'tryp 0 '+arg
				
				#arg='if <ischar>\n\ttryp 0 '+arg+'elif <topobj>\n\tif <topobj.ischar>\n\t\ttopobj.tryp 0 '+arg+'\tendif\nelif <link>\n\tif <link.ischar>\n\t\tlink.tryp 0 '+arg+'\telse\n\t\t'+arg+'\tendif\nelse\n\t'+arg+'endif\n'
			arg=self.replaceBrackets(arg)
		arg=self.translateKnownArrayDefNames(arg)			
		if self.writeToExtraText==1:
			self.extraText.append(arg)
		else:
			self.scp.write(arg)
			
	#Parse one line of a file.
	def parseline(self,line):
		self.defnameParse=1
		if self.includeOriginalCode:
			self.scp_write('//'+line+'\n')
		strline = line
		commentPos = self.finds(strline,'#',0)
		if commentPos>-1:
			if strline.lower()=="#produce-readable-code":
				self.produceReadableCode=1
			if strline.lower()=="#include-original-code":
				self.includeOriginalCode=1
			elif strline.lower()=="#omit-original-code":
				self.includeOriginalCode=0
			
			if strline.strip().lower()=="#enable-replace":
				self.enableReplacer=1
			elif strline.strip().lower()=="#disable-replace":
				self.enableReplacer=0
			
			if strline.lower()=="#prefix-sphere":
				self.prefixSphere=1
			if strline.lower()=="#prefix-auto":
				self.prefixAuto=1
			elif strline.lower()=="#prefix-local":
				self.prefixLocal=1
			if strline.lower()=="#exclude-quotes":
				self.excludeQuotes=1
			sharppos = self.finds(strline,'#',0)
			ischarpos=strline.lower().find("is char\n")
			if ischarpos>-1:
				self.whatischar=strline[sharppos+1:ischarpos]+'.'
				if self.whatischar=='self.':
					self.whatischar=''
			if len(strline)>8 and strline[:8].lower()=="#sphere-":
				self.sphereVer=strline[8:]
				if self.supports[self.sphereVer]['<??>']:
					self.evalStartChar='<?'
					self.evalEndChar='?>'
				else:
					self.evalStartChar='<'
					self.evalEndChar='>'
				
			strline=strline[:commentPos]
		if len(strline)==0:
			return ""
		while strline[-1:]=='\t' or strline[-1:]==' ':
			strline=strline[:-1]
		if not hasContent(strline):
			return ""
		numTabs = self.countTabs(strline)
		if len(strline[numTabs:])==0:
			return ""
		
		if self.inScriptDef==5:
			if numTabs==2:
				paren = strline.find('(')
				if paren>-1:
					paren2 = self.findn(strline,')',paren)
					argtxt = strline[paren+1:paren2]
					args = self.split(argtxt,',')
					self.functionName=strline[2:paren]
					if self.functionName.lower()=='addtext':
						if len(args)==0:
							raise SystemExit,"Missing argument to addText. See PySphere/scripts/dialogs.py. (Error on line "+str(self.lineNum)+' of '+self.moduleName+'.py)'
						elif len(args)>1:
							raise SystemExit,"Too many arguments to addText. See PySphere/scripts/dialogs.py. (Error on line "+str(self.lineNum)+' of '+self.moduleName+'.py)'
						else:
							self.writeToExtraText=0
							self.scp_write('textA(35,'+self.evalStartChar+'argo.tag.ytextpos'+self.evalEndChar+','+str(self.textColor)+',"'+self.translateParam(args[0])+'")\n')
							self.scp_write('argo.f_'+self.curdialogname+'_py\n');
							return
					elif self.functionName.lower()=='addentry':
						if len(args)<2:
							raise SystemExit,"Missing arguments to addEntry. See PySphere/scripts/dialogs.py. (Error on line "+str(self.lineNum)+' of '+self.moduleName+'.py)'
						elif len(args)==2:
							self.writeToExtraText=0
							self.scp_write('textA(35,'+self.evalStartChar+'argo.tag.ytextpos'+self.evalEndChar+','+str(self.textColor)+',"'+self.translateParam(args[0])+'")\n')
							self.buttonnum+=1
							#0845, 521, 0x209	+1
							#08af, 568, 0x238
							#08b0, 569, 0x239
							#0fa5, 867, 0x363	+2
							#0fae, 876, 0x36c	+2
							
							self.scp_write('argo.button(15,'+self.evalStartChar+'argo.tag.ytextpos'+self.evalEndChar+'+5,2117,2118,1,'+self.evalStartChar+'argo.tag.pagenum'+self.evalEndChar+','+str(self.buttonnum)+')\n')
							self.scp_write('argo.f_'+self.curdialogname+'_py\n');
							self.writeToExtraText=1
							self.scp_write('onbutton='+str(self.buttonnum)+'\n')
							self.scp_write(self.translateParam(args[1])+'\n')
							self.writeToExtraText=0
							return
						else:
							self.writeToExtraText=0
							self.scp_write('textA(35,'+self.evalStartChar+'argo.tag.ytextpos'+self.evalEndChar+','+str(self.textColor)+',"'+self.translateParam(args[0])+'")\n')
							self.buttonnum+=1
							self.scp_write('argo.button(15,'+self.evalStartChar+'argo.tag.ytextpos'+self.evalEndChar+'+5,2117,2118,1,'+self.evalStartChar+'argo.tag.pagenum'+self.evalEndChar+','+str(self.buttonnum)+')\n')
							self.scp_write('argo.f_'+self.curdialogname+'_py\n');
							self.writeToExtraText=1
							self.scp_write('onbutton='+str(self.buttonnum)+'\n')
							self.scp_write(self.translateParam(args[1])+'('+self.translateParam(args[2]))
							for a in range(3,len(args)):
								self.scp_write(','+self.translateParam(args[a]))
							self.scp_write(')\n')
							self.writeToExtraText=0
					elif self.functionName.lower()=='textcolor':
						if len(args)!=1:
							raise SystemExit,"TextColor should only have one argument. See PySphere/scripts/dialogs.py. (Error on line "+str(self.lineNum)+' of '+self.moduleName+'.py)'
						else:
							try:
								self.textColor=int(args[0])
							except ValueError:
								raise SystemExit,"Invalid TextColor "+args[0]+". See PySphere/scripts/dialogs.py. (Error on line "+str(self.lineNum)+' of '+self.moduleName+'.py)'
								
					#else:
					#	self.scp_write('eh... '+self.functionName.lower())
				else:
					raise SystemExit,"Missing arguments, or def main in menuDialog blocks must consist entirely of addText and addEntry function calls. See PySphere/scripts/dialogs.py. (Error on line "+str(self.lineNum)+' of '+self.moduleName+'.py)'
				return
			elif numTabs>2:
				raise SystemExit,"def main in menuDialog blocks must consist entirely of addText and addEntry function calls. See PySphere/scripts/dialogs.py. (Error on line "+str(self.lineNum)+' of '+self.moduleName+'.py)'
		
		if len(strline)>4:
			if strline[:4].lower()=='def ':
				#function definition. Not tabbed, so NOT a trigger definition
				self.inScriptDef=0
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				self.functionName = strline[3:].strip()
				args = None
				colon = self.functionName.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				paren = self.functionName.find('(')
				if paren>-1:
					paren2 = self.findn(self.functionName,')',paren)
					argtxt = self.functionName[paren+1:paren2]
					args = self.split(argtxt,',')
					self.functionName=self.functionName[:paren]
				else:
					self.functionName=self.functionName[:colon]					
				self.scp_write('[function '+self.functionName+']\n')
				if args!=None:
					num=0
					for arg in args:
						arg=arg.strip()
						if self.prefixLocal==1 and arg.lower().find('local.')==0:
							arg=arg[6:].strip()
						eqpos = arg.find('=')
						defval=None
						if eqpos>-1:
							defval=arg[eqpos+1:].strip()
							arg=arg[:eqpos].strip()
							
						if self.supports[self.sphereVer]['functionParameters']:
							#commented out code here is from R8-, new code R9+ ('self.eval[Start|End]Char' is R15+)
							#self.scp_write(self.varheader()+arg+'=<argv['+str(num)+']>\n')
							self.scp.write(self.generateLocalSet(arg,self.evalStartChar+'argv['+str(num)+']'+self.evalEndChar, 1))
						else:
							#commented out code here is from R8-, new code R9+ ('self.eval[Start|End]Char' is R15+)
							#self.scp.write(self.varheader()+arg+'=<var.'+arg+'>\n')
							#self.scp.write('var.'+arg+'=\n')
							self.scp.write(self.generateLocalSet(arg,self.evalStartChar+'var.'+arg+self.evalEndChar, 1))
							
						if defval!=None:
							#commented out code here is from R8-, new code R9+ ('self.eval[Start|End]Char' is R15+)
							#self.scp.write('if (!(strlen(<'+self.varheader()+arg+'>)))\n')
							#self.scp.write(self.varheader()+arg+'='+self.translateParam(defval)+'\nendif\n')
							self.scp.write('if (!(strlen('+self.evalStartChar+self.generateLocalGet(arg)+self.evalEndChar+')))\n')
							self.scp.write(self.generateLocalSet(arg,self.translateParam(defval), 1))
							self.scp.write('endif\n')
						num+=1
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				return
			elif strline[:5].lower()=='\tdef ':
				#Trigger.
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				self.functionName = strline[4:colon].strip()
				paren = self.functionName.find('(')
				functionArgs=None
				if paren>-1:
					if self.functionName.find('()')!=paren:
						if self.inScriptDef==3:
							rParen=self.functionName.find(')')
							functionArgs=self.functionName[paren+1:rParen]
							self.functionName=self.functionName[:paren].strip()
						elif self.inScriptDef==4:
							rParen=self.functionName.find(')')
							functionArgs=self.translateParam(self.functionName[paren+1:rParen])
							self.functionName=self.functionName[:paren].strip()
						else:
							raise SystemExit,"Trigger definitions shouldn't have arguments: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
					else:
						self.functionName=self.functionName[:paren]
				#asdfasdfasdfasdf
				
				if self.inScriptDef==5 and self.functionName=='main':
					self.writeToExtraText=1
					self.blocks.append('')
					self.extraTextBlocks.append(('',1))
					self.blockTab+=1
				else:
					try:
						buttonNum=int(self.functionName)
						if functionArgs==None:
							self.scp_write('on='+self.functionName+'\n')
						else:
							self.scp_write('on='+self.functionName+' '+functionArgs+'\n')
					except ValueError:
						if functionArgs==None:
							self.scp_write('on=@'+self.functionName+'\n')
						else:
							self.scp_write('on=@'+self.functionName+' '+functionArgs+'\n')
					self.blocks.append('')
					self.extraTextBlocks.append(('',0))
					self.blockTab+=1
				return
			elif numTabs==1 and self.inScriptDef==1:
				#Init on a def
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				self.scp_write(strline[1:]+'\n')
				return
			elif numTabs==1 and self.inScriptDef==2:
				#value in a defname
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				self.scp_write(strline[1:].replace('=','\t\t').replace('[','_').replace(']','\t')+'\n')
				return
			elif strline[:8].lower()=='itemdef ' or strline[:8].lower()=='chardef ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (ITEMDEF)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[8:colon].strip()
					param=None
					if (strline[:8].lower()=='itemdef '):
						corrected=strline[:8]+idname+'(i_gold):'
					else:
						corrected=strline[:8]+idname+'(c_man):'
					raise SystemExit,'Missing base-class in itemdef or chardef on line '+str(self.lineNum)+' of '+self.moduleName+'.py.\n\t'+strline+'\nshould be:\n\t'+corrected
				elif lparen>-1 and rparen>-1 and rparen>lparen:
					idname=strline[8:lparen].strip()
					param=strline[lparen+1:rparen].strip()
				else:
					raise SystemExit,'Bad '+strline[:8].lower()+'on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				self.scp_write('['+strline[:7].lower()+' '+idname+']\n')
				if string.digits.find(idname[0])>-1:
					if string.digits.find(param[0])>-1:
						raise SystemExit,'Bad '+strline[:8].lower()+'on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
					else:
						self.scp.write('defname='+param+'\n')
				else:
					self.scp.write('id='+param+'\n')
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=1
				return
			elif strline[:8].lower()=='typedef ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (TYPEDEF)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[8:colon].strip()
				else:
					raise SystemExit,'Bad typedef on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				self.scp_write('[typedef '+idname+']\n')
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=1
				return
			elif strline[:7].lower()=='events ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (EVENTS)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[7:colon].strip()
				else:
					raise SystemExit,'Bad event on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				self.scp_write('[events '+idname+']\n')
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=1
				return
			elif strline[:6].lower()=='event ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (EVENT)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[6:colon].strip()
				else:
					raise SystemExit,'Bad event on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				self.scp_write('[events '+idname+']\n')
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=1
				return
			elif strline[:6].lower()=='plevel':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (DEFNAME)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					raise SystemExit,"plevel statement should be plevel(1): (Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				else:
					idname=strline[lparen+1:rparen]
				self.scp_write('[plevel '+idname+']\n')
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=1
				return
			elif strline[:8].lower()=='defname ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (DEFNAME)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[8:colon].strip()
				else:
					raise SystemExit,'Bad defname on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				self.scp_write('[defnames '+idname+']\n')
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=2
				return
			elif strline[:9].lower()=='defnames ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (DEFNAMES)' 
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[9:colon].strip()
				else:
					raise SystemExit,'Bad defnames on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				self.scp_write('[defnames '+idname+']\n')
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=2
				return
			elif strline[:7].lower()=='dialog ':
				#dialog definition.
				self.inScriptDef=0
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				self.functionName = strline[7:].strip()
				args = None
				colon = self.functionName.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of dialog: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				paren = self.functionName.find('(')
				if paren>-1:
					paren2 = self.findn(self.functionName,')',paren)
					argtxt = self.functionName[paren+1:paren2]
					args = self.split(argtxt,',')
					self.functionName=self.functionName[:paren]
				else:
					self.functionName=self.functionName[:colon]					
				self.scp_write('[dialog '+self.functionName+']\n')
				if args!=None:
					num=0
					for arg in args:
						arg=arg.strip()
						if self.prefixLocal==1 and arg.lower().find('local.')==0:
							arg=arg[6:].strip()
						eqpos = arg.find('=')
						defval=None
						if eqpos>-1:
							defval=arg[eqpos+1:].strip()
							arg=arg[:eqpos].strip()
							
						self.scp.write(self.generateLocalSet(arg,self.evalStartChar+'argv['+str(num)+']'+self.evalEndChar, 1))
							
						if defval!=None:
							#commented out code here is from R8-, new code R9+ ('self.eval[Start|End]Char' is R15+)
							#self.scp.write('if (!(strlen(<'+self.varheader()+arg+'>)))\n')
							#self.scp.write(self.varheader()+arg+'='+self.translateParam(defval)+'\nendif\n')
							self.scp.write('if (!(strlen('+self.evalStartChar+self.generateLocalGet(arg)+self.evalEndChar+')))\n')
							self.scp.write(self.generateLocalSet(arg,self.translateParam(defval), 1))
							self.scp.write('endif\n')
						num+=1
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				return
			elif strline[:13].lower()=='dialogbutton ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (EVENTS)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[13:colon].strip()
				else:
					raise SystemExit,'Bad dialogbutton block on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				self.scp_write('[DIALOG '+idname+' BUTTON]\n')
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=1
				return
			elif strline[:12].lower()=='contextmenu ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (EVENTS)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[12:colon].strip()
					self.scp_write('[MENU '+idname+']\n')
				else:
					idname=strline[12:lparen].strip()
					txt=strline[lparen+1:rparen].strip()
					self.scp_write('[MENU '+idname+']\n')
					self.scp_write(self.translateParam(txt)+'\n')
					#raise SystemExit,'Bad event on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=3
				return
			elif strline[:5].lower()=='menu ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (EVENTS)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[5:colon].strip()
					self.scp_write('[MENU '+idname+']\n')
				else:
					idname=strline[5:lparen].strip()
					txt=strline[lparen+1:rparen].strip()
					self.scp_write('[MENU '+idname+']\n')
					self.scp_write(self.translateParam(txt)+'\n')
					#raise SystemExit,'Bad event on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
					
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.inScriptDef=4
				return
			elif strline[:11].lower()=='menudialog ':
				while numTabs<self.blockTab:
					st = self.blocks.pop()
					if st!=None:
						self.scp_write(st)
					st = self.extraTextBlocks.pop()
					if st[0]!=None:
						self.extraText.append(st[0])
					if st[1]==1:
						self.writeToExtraText=0
					self.blockTab-=1
				lparen = strline.find('(')
				if lparen>-1:
					rparen = self.findn(strline,')',lparen)
				else:
					rparen=-1
					#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (EVENTS)'
				colon = strline.find(':')
				if colon==-1:
					raise SystemExit,"Missing colon at the end of def: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
				
				if lparen==-1 and rparen==-1:
					idname=strline[11:colon].strip()
				else:
					if rparen==lparen+1:
						idname=strline[11:lparen].strip()
					else:
						raise SystemExit,'Bad menudialog on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				self.writeToExtraText=1
				self.curdialogname=idname
				self.textColor=1152
				self.scp_write('[FUNCTION f_'+idname+'_py]\n')
				self.scp_write('tag.ytextpos='+self.evalStartChar+'tag.ytextpos'+self.evalEndChar+'+20\n')
				self.scp_write('if ('+self.evalStartChar+'tag.ytextpos'+self.evalEndChar+'>440)\n')
				self.scp_write('tag.ytextpos=5\n')
				self.scp_write('button(570,0,4005,4007,0,<?eval ('+self.evalStartChar+'tag.pagenum'+self.evalEndChar+'+1)?>,0)\n')
				self.scp_write('tag.pagenum='+self.evalStartChar+'tag.pagenum'+self.evalEndChar+'+1\n')
				self.scp_write('page='+self.evalStartChar+'tag.pagenum'+self.evalEndChar+'\n')
				self.scp_write('button(0,0,4014,4015,0,<?eval ('+self.evalStartChar+'tag.pagenum'+self.evalEndChar+'-1)?>,0)\n')
				self.scp_write('endif\n')
				
				self.scp_write('[DIALOG '+idname+' BUTTON]\n')
				self.writeToExtraText=0
				self.scp_write('[DIALOG '+idname+']\n')
				self.scp_write('SetLocation=10,30\n')
				self.scp_write('argo.page=0\n')
				self.scp_write('resizepic(0,0,2620,600,450)\n')
				self.scp_write('argo.tag.ytextpos=5\n')
				self.scp_write('argo.tag.pagenum=1\n')
				self.scp_write('argo.page=1\n')
				self.blocks.append('')
				self.extraTextBlocks.append(('',0))
				self.blockTab+=1
				self.buttonnum=0
				self.inScriptDef=5
				#addtext
				#addentry
				return
			
			
		if len(strline)>1:
			if strline[:1]=='\t':
				#special cases
				if numTabs>self.blockTab:
					raise SystemExit,'Unexpected indentation on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				strline=strline[numTabs:]
				ifpos=strline.find('if ')
				elifpos=strline.find('elif ')
				elsepos=strline.find('else')
				whilepos=strline.find('while ')
				forpos=strline.find('for ')

				if strline.strip().find('if ')==0:
					self.defnameParse=0
					strline = strline.replace(' and ',' && ')
					strline = strline.replace(' or ',' || ')
					strline = strline.replace(' not ',' !')
					colon = strline.rfind(':')
					if colon==-1:
						raise SystemExit,"Missing colon at the end of if: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
					while self.blockTab>numTabs:
						st = self.blocks.pop()
						if st!=None:
							self.scp_write(st)
						st = self.extraTextBlocks.pop()
						if st[0]!=None:
							self.extraText.append(st[0])
						if st[1]==1:
							self.writeToExtraText=0
						self.blockTab-=1
					self.generateBlock('if', condition=strline[ifpos+3:colon])
					return
				elif strline.strip().find('elif ')==0:
					self.defnameParse=0
					strline = strline.replace(' and ',' && ')
					strline = strline.replace(' or ',' || ')
					strline = strline.replace(' not ',' !')
					colon = strline.rfind(':')
					if colon==-1:
						raise SystemExit,"Missing colon at the end of elif: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
					while self.blockTab>numTabs+1:
						st = self.blocks.pop()
						if st!=None:
							self.scp_write(st)
						st = self.extraTextBlocks.pop()
						if st[0]!=None:
							self.extraText.append(st[0])
						if st[1]==1:
							self.writeToExtraText=0
						self.blockTab-=1
					tt=self.translateParam(strline[elifpos+5:colon])
					if tt.__class__==tuple:
						tt=tt[0]
					self.scp_write('ELIF '+tt+'\n')
					return
				elif strline.strip().find('else')==0:
					colon = strline.rfind(':')
					if colon==-1:
						raise SystemExit,"Missing colon at the end of elif: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
					while self.blockTab>numTabs+1:
						st = self.blocks.pop()
						if st!=None:
							self.scp_write(st)
						st = self.extraTextBlocks.pop()
						if st[0]!=None:
							self.extraText.append(st[0])
						if st[1]==1:
							self.writeToExtraText=0
						self.blockTab-=1
					self.scp_write('ELSE\n')
					return
				elif strline.strip().find('while ')==0:
					self.defnameParse=0
					strline = strline.replace(' and ',' && ')
					strline = strline.replace(' or ',' || ')
					strline = strline.replace(' not ',' !')
					colon = strline.rfind(':')
					if colon==-1:
						raise SystemExit,"Missing colon at the end of while: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
					while self.blockTab>numTabs:
						st = self.blocks.pop()
						if st!=None:
							self.scp_write(st)
						st = self.extraTextBlocks.pop()
						if st[0]!=None:
							self.extraText.append(st[0])
						if st[1]==1:
							self.writeToExtraText=0
						self.blockTab-=1
					self.generateBlock('while', condition=strline[whilepos+6:colon])
					return
				elif strline.strip().find('doswitch ')==0:
					dopos = strline.find('doswitch ')
					colon = strline.rfind(':')
					if colon>-1:
						varname=strline[dopos+9:colon].strip()
						
						strn='doswitch '+self.translateParam(varname)+'\n'
						
						while self.blockTab>numTabs:
							st = self.blocks.pop()
							if st!=None:
								self.scp_write(st)
							st = self.extraTextBlocks.pop()
							if st[0]!=None:
								self.extraText.append(st[0])
							if st[1]==1:
								self.writeToExtraText=0
							self.blockTab-=1
						self.blocks.append('enddo\n')
						self.extraTextBlocks.append(('',0))
						self.blockTab+=1
						self.scp_write(strn)
					else:
						raise SystemExit,"Invalid for loop on line "+str(self.lineNum)+' of '+self.moduleName+'.py. Example: for a in range(0,10)'
					return
				elif strline.strip().find('dorand ')==0:
					dopos = strline.find('dorand ')
					colon = strline.rfind(':')
					if colon>-1:
						varname=strline[dopos+7:colon].strip()
						
						strn='dorand '+self.translateParam(varname)+'\n'
						
						while self.blockTab>numTabs:
							st = self.blocks.pop()
							if st!=None:
								self.scp_write(st)
							st = self.extraTextBlocks.pop()
							if st[0]!=None:
								self.extraText.append(st[0])
							if st[1]==1:
								self.writeToExtraText=0
							self.blockTab-=1
						self.blocks.append('enddo\n')
						self.extraTextBlocks.append(('',0))
						self.blockTab+=1
						self.scp_write(strn)
					else:
						raise SystemExit,"Invalid for loop on line "+str(self.lineNum)+' of '+self.moduleName+'.py. Example: for a in range(0,10)'
					return
				elif strline.strip().find('for ')==0:
					self.defnameParse=0
					inr=strline.find(' in ')
					if inr>-1:
						ranger=strline.find(' range')
						if ranger>-1:
							forr=strline.find('for ')
							lparen=strline.find('(')
							comma=strline.find(',',lparen)
							rparen=self.findn(strline,')',lparen)
							if forr>-1 and lparen>-1 and comma>-1 and rparen>-1:
								varname=strline[forr+4:inr].strip()
								startVal=strline[lparen+1:comma]
								endVal=strline[comma+1:rparen]
								comma2=strline.find(',',comma+1)
								stepVal=1
								if (comma2!=-1 and comma2<rparen):
									endVal=strline[comma+1:comma2]
									stepVal=strline[comma2+1:rparen]
									try:
										stepVal=int(stepVal)
									except ValueError:
										raise SystemExit,"\n\tCannot translate for...range statement with a dynamic step.\n\tStep must be an integer !=0. (Line "+str(self.lineNum)+' of '+self.moduleName+'.py.)'
								colon = strline.rfind(':')
								if colon>-1:
									while self.blockTab>numTabs:
										st = self.blocks.pop()
										if st!=None:
											self.scp_write(st)
										st = self.extraTextBlocks.pop()
										if st[0]!=None:
											self.extraText.append(st[0])
										if st[1]==1:
											self.writeToExtraText=0
										self.blockTab-=1
									if stepVal>0:
										self.generateBlock('forrange', varname=varname, minval=startVal, maxval=endVal, condition=str(stepVal), noparseCondition=1)
									elif stepVal<0:
										self.generateBlock('forrangerev', varname=varname, minval=startVal, maxval=endVal, condition=str(-stepVal), noparseCondition=1)
								else:
									raise SystemExit,"Missing colon at the end of for: Line "+str(self.lineNum)+' of '+self.moduleName+'.py.'
							else:
								raise SystemExit,"Invalid for loop on line "+str(self.lineNum)+' of '+self.moduleName+'.py. Example: for a in range(0,10)'
						else:
							#for var in array:
							forr=strline.find('for ')
							colon = strline.rfind(':')
							if forr>-1 and colon>-1:
								varname=strline[forr+4:inr].strip()
								arrayname=strline[inr+4:colon].strip()
								tt=self.translateParam(varname+'__val')
								if tt.__class__==tuple:
									tt=tt[0]
								
								strn=self.stripLTGT(self.translateParam(varname+'__val'))+"="+tt+"+1\n"
								
								tt=self.translateParam(arrayname+'['+varname+'__val'+"]")
								if tt.__class__==tuple:
									tt=tt[0]
								strn+=self.stripLTGT(self.translateParam(varname))+"="+tt+"\n"
								while self.blockTab>numTabs:
									st = self.blocks.pop()
									if st!=None:
										self.scp_write(st)
									st = self.extraTextBlocks.pop()
									if st[0]!=None:
										self.extraText.append(st[0])
									if st[1]==1:
										self.writeToExtraText=0
									self.blockTab-=1
								self.generateBlock('forarray', varname=varname, arrayname=arrayname)
							else:
								raise SystemExit,"Invalid for loop on line "+str(self.lineNum)+' of '+self.moduleName+'.py. Example: for a in range(0,10)'
					else:
						raise SystemExit,"Missing 'in' keyword in for statement on line "+str(self.lineNum)+' of '+self.moduleName+'.py. Example: for a in range(0,10)'
					return
				else:
					while numTabs<self.blockTab:
						st = self.blocks.pop()
						if st!=None:
							self.scp_write(st)
						st = self.extraTextBlocks.pop()
						if st[0]!=None:
							self.extraText.append(st[0])
						if st[1]==1:
							self.writeToExtraText=0
						self.blockTab-=1
					equals = strline.find('=')
					if equals>-1 and not self.inquote(strline,equals):
						#variable assignment
						if equals==0:
							raise SystemExit,'WTF is line '+str(self.lineNum)+' of '+self.moduleName+'.py supposed to be?'
						else:
							tfndstr='+-*/%'
							tfnd=string.find(tfndstr,strline[equals-1])
							if tfnd>-1:
								tta=self.translateParam(strline[:equals-1])
								if tta.__class__==tuple:
									tta=tta[0]
								ttb=self.translateParam(strline[equals+1:])
								if ttb.__class__==tuple:
									ttb=ttb[0]
								sss=self.translateParam(strline[:equals-1])
								sss=self.stripLTGT(sss)
								if sss.find('ARG(')==0 and sss[-1]==')':
									if self.supports[self.sphereVer]['#']:
										self.scp_write(sss[:-1]+",#"+tfndstr[tfnd]+ttb+')\n')
									else:
										self.scp_write(sss[:-1]+","+tta+tfndstr[tfnd]+ttb+')\n')
								else:
									self.scp_write(self.stripLTGT(self.translateParam(strline[:equals-1]))+"="+tta+tfndstr[tfnd]+ttb+'\n')
							else:
								tt=self.translateParam(strline[equals+1:].strip())
								if tt.__class__==tuple:
									tt=tt[0]
								sss=self.stripLTGT(self.translateParam(strline[:equals].strip()))
								if sss.find('ARG(')==0 and sss[-1]==')':
									self.scp_write(sss[:-1]+","+tt+')\n')
								else:
									self.scp_write(sss+"="+tt+'\n')
					else:
						self.scp_write(self.stripLTGT(self.translateParam(strline))+'\n')
						#command or function call
		while numTabs<self.blockTab:
			st = self.blocks.pop()
			if st!=None:
				self.scp_write(st)
			st = self.extraTextBlocks.pop()
			if st[0]!=None:
				self.extraText.append(st[0])
			if st[1]==1:
				self.writeToExtraText=0
			self.blockTab-=1
	
	#returns true if whatever's at 'pos' is inside a string. This is used so we can correctly detect assignment,
	#as opposed to someone saying sysmessage("Your color="+color). *wink*
	def inquote(self, arg, pos):
		retval=0
		start=0
		stringstart=None
		stringstartchar=None
		for a in range(0,len(arg)):
			if arg[a]=='"' or arg[a]=="'":
				if stringstart==None:
					stringstart=a
					stringend=None
					stringstartchar=arg[a]
				elif arg[a]==stringstartchar:
					stringstart=None
			if pos==a:
				if stringstart==None:
					return 0
				else:
					return 1
		return 0
		
	def replaceBrackets(self, arg):
		retval=''
		start=0
		stringstart=None
		stringstartchar=None
		argst = arg.strip()
		if len(argst)>0 and argst[0]=='[':
			return arg
		for a in range(0,len(arg)):
			if arg[a]==']' and stringstart==None:
				retval+=arg[start:a]
				start=a+1
			elif arg[a]=='[' and stringstart==None:
				retval+=arg[start:a]
				retval+='_'
				start=a+1
			elif arg[a]=='"' or arg[a]=="'":
				if stringstart==None:
					stringstart=a
					stringend=None
					stringstartchar=arg[a]
				elif arg[a]==stringstartchar:
					stringstart=None	
		lastarg=arg[start:]
		if len(lastarg)>0:
			retval+=lastarg
		return retval
	
	def findn(self, arg, findchar, startat):
		retval=-1
		if len(arg)<=startat:
			return -1
		recursechar=arg[startat]
		stringstart=None
		stringstartchar=None
		recurses=0
		for a in range(startat+1,len(arg)):
			if arg[a]==findchar:
				if stringstart==None:
					if recurses==0:
						return a
					else:
						recurses-=1
			elif arg[a]==recursechar:
				if stringstart==None:
					recurses+=1
			elif arg[a]=='"' or arg[a]=="'":
				if stringstart==None:
					stringstart=a
					stringend=None
					stringstartchar=arg[a]
				elif arg[a]==stringstartchar:
					if arg[a-1]=="\\":
						pass
					else:
						stringstart=None
		return -1
		
	def finds(self, arg, findchar, startat):
		retval=-1
		if len(arg)<=startat:
			return -1
		stringstart=None
		stringstartchar=None
		for a in range(startat,len(arg)):
			if arg[a]==findchar:
				if stringstart==None:
					return a
			elif arg[a]=='"' or arg[a]=="'":
				if stringstart==None:
					stringstart=a
					stringend=None
					stringstartchar=arg[a]
				elif arg[a]==stringstartchar:
					if arg[a-1]=="\\":
						pass
					else:
						stringstart=None
		return -1
	
	def replace(self, arg, frm, to):
		#print 'replacing '+frm+' with '+to+' in '+arg+'.'
		retval=arg
		comment=retval.find('//')
		mins=0
		frmpos = retval.lower().find(frm,mins)
		frminto = to.lower().find(frm)
		topos = retval.lower().find(to,frmpos-frminto)
		while topos+frminto==frmpos and frmpos>-1:
			mins=frmpos+len(frm)
			frmpos = retval.lower().find(frm,mins)
			frminto = to.lower().find(frm)
			topos = retval.lower().find(to,frmpos-frminto)
			comment=retval.find('//')
			
		while frmpos>-1 and (comment==-1 or comment>frmpos):
			if not self.inquote(retval,frmpos):
				retval = retval[0:frmpos]+to+retval[frmpos+len(frm):]
				mins=frmpos+len(to)
			mins+=1
			frmpos = retval.lower().find(frm,mins)
			comment=retval.find('//')
		return retval
		
	#This is a custom split function, which splits by commas, but recognizes strings and ignores commas in them.
	def split(self, arg, splitby):
		recurses=0
		retval=[]
		start=0
		stringstart=None
		stringstartchar=None
		for a in range(0,len(arg)):
			if arg[a]==')':
				if stringstart==None:
					if recurses>=0:
						recurses-=1
			elif arg[a]=='(':
				if stringstart==None:
					recurses+=1
			elif arg[a]==',':
				if stringstart==None and recurses==0:
					retval.append(arg[start:a])
					start=a+1
			elif arg[a]=='"' or arg[a]=="'":
				if stringstart==None:
					stringstart=a
					stringend=None
					stringstartchar=arg[a]
				elif arg[a]==stringstartchar:
					if arg[a-1]=="\\":
						pass
					else:
						stringstart=None
		lastarg=arg[start:]
		if len(lastarg)>0:
			retval.append(lastarg)
		return retval
	
	#This counts the number of tabs preceding the code on a line.
	def countTabs(self, arg):
		numTabs=0
		for a in arg:
			if a=='\t':
				numTabs+=1
			else:
				return numTabs
		return numTabs
	
	#This removes the <>s surrounding arg, if there are any.
	def stripLTGT(self, arg):
		tt=arg
		startpos=0
		if tt.__class__==tuple:
			startpos=tt[1]
			tt=tt[0]
		retval = tt
		if retval[startpos:startpos+1]=='<':
			if retval[startpos+1:startpos+2]=='?':
				retval=retval[:startpos]+retval[startpos+2:]
			else:
				retval=retval[:startpos]+retval[startpos+1:]
		if retval[-1:]=='>':
			if retval[-2]=='?':
				retval=retval[:-2]
			else:
				retval=retval[:-1]
			
		return retval
	
	#This removes the ()s surrounding arg, if there are any.
	def stripLPGP(self, arg):
		tt=arg
		startpos=0
		if tt.__class__==tuple:
			startpos=tt[1]
			tt=tt[0]
		retval = tt
		if retval[startpos:startpos+1]==')':
			retval=retval[:startpos]+retval[startpos+1:]
		if retval[-1:]==')':
			retval=retval[:-1]
		return retval
	
	#This is called when the compiler sees something like something(arg,arg,arg,arg,ARG!) in your script.
	#It's called once for every 'arg'. So, if the compiler sees myFunc(local.bob,"dole"+5), it will run for local.bob
	#and for "dole"+5.
	
	#This is really big and complicated. Read at your own peril.
	def translateParam(self, arg):
		retstr = ''
		retpos = None
		stringstart=None
		stringend=None
		stringstartchar=None
		varstart=None
		varend=None
		hexstart=None
		decstart=None
		recurseLvl=0
		while len(arg)>=1 and arg[0]=='\t':
			arg=arg[1:]
		for a in range(0,len(arg)):
			if varstart!=None and varend==None and string.letters.find(arg[a])==-1 and arg[a]!='_' and string.digits.find(arg[a])==-1:
				if arg[a]=='(' or arg[a]=='[':
					recurseLvl+=1
				elif arg[a]==')' or arg[a]==']':
					if recurseLvl>0:
						recurseLvl-=1
					elif arg[a]==')':
						#end var!
						varpart = arg[varstart:a]
						varstart=None
						varend=a
						if self.prefixAuto==1:
							retstr,varpart = self.parsePrefixAuto(varpart, retstr)
						elif (self.prefixSphere==1 and varpart.lower().find('sphere.')!=0) or (self.prefixLocal==1 and varpart.lower().find('local.')==0):
							localRemoved=0
							if self.prefixLocal==1 and varpart.lower().find('local.')==0:
								varpart=varpart[6:]
								localRemoved=1
							retstr = self.parseVariable(retstr, varpart,localRemoved,-1)
								
						else:
							#if (self.prefixSphere==1 and varpart.lower().find('sphere.')!=0) or (self.prefixLocal==1 and varpart.lower().find('local.')==0):
							sphereRemoved=0
							if self.prefixSphere==1 and varpart.lower().find('sphere.')==0:
								varpart=varpart[7:]
								sphereRemoved=1
							#calling command on an object, or non-local variable
							retstr = self.parseVariable(retstr, varpart,-1,sphereRemoved)	
				if arg[a]!='.' and arg[a]!=')' and arg[a]!=']' and recurseLvl==0 and not (a>0 and arg[a]=='<' and (arg[a-1]=='.' or arg[a-1]=='(' or arg[a-1]=='[' or arg[a-1]==']')) and not (len(arg)>a+1 and arg[a]=='>' and (arg[a+1]=='.' or arg[a+1]=='(' or arg[a+1]=='[' or arg[a+1]==']')):
					varpart = arg[varstart:a]
					varstart=None
					varend=a
					if self.prefixAuto==1:
						retstr,varpart = self.parsePrefixAuto(varpart, retstr)
					elif (self.prefixSphere==1 and varpart.lower().find('sphere.')!=0) or (self.prefixLocal==1 and varpart.lower().find('local.')==0):
						localRemoved=0
						if self.prefixLocal==1 and varpart.lower().find('local.')==0:
							varpart=varpart[6:]
							localRemoved=1
						retstr = self.parseVariable(retstr, varpart,localRemoved,-1)
							
					else:
						#if (self.prefixSphere==1 and varpart.lower().find('sphere.')!=0) or (self.prefixLocal==1 and varpart.lower().find('local.')==0):
						sphereRemoved=0
						if self.prefixSphere==1 and varpart.lower().find('sphere.')==0:
							varpart=varpart[7:]
							sphereRemoved=1
						#calling command on an object, or non-local variable
						retstr = self.parseVariable(retstr, varpart,-1,sphereRemoved)	
			elif hexstart!=None and string.hexdigits.find(arg[a].upper())==-1:
				hexstart=None
			elif decstart!=None and string.digits.find(arg[a])==-1:
				decstart=None
			
			if varstart!=None:
				pass
			elif stringstart!=None:
				if (arg[a]=='"' or arg[a]=="'") and stringstartchar==arg[a]:
					if arg[a-1]=="\\":
						retstr+=arg[stringstart:a-1]+arg[a]
						stringstart=a+1
					else:
						#end string
						partstr = arg[stringstart:a]
						if self.excludeQuotes==0:
							if partstr.find(',')>-1:
								partstr='"'+partstr+'"'
						retstr+=partstr
						stringstart=None
						stringend=a
			elif arg[a]=='+' and stringend==a-1:
				#("your name is "+src.name) --> (your name is <src.name>)
				#passing is all we have to do. We ignore this character.
				pass
			elif arg[a]=='"' or arg[a]=="'":
				if stringstart==None:
					#start string
					stringstart=a+1 #+self.excludeQuotes
					stringstartchar=arg[a]
					stringend=None
					#if self.excludeQuotes==0:
					#	retstr+='"'
					#check for + before the string
					if retstr[-1:]=='+':
						retstr=retstr[:-1]
			elif arg[a]=='0' and stringstart==None and varstart==None:
				#hex num started here
				if decstart==None and hexstart==None:
					hexstart=a
				retstr+=arg[a]
			elif string.digits.find(arg[a])>-1:
				#numbers
				if hexstart==None and decstart==None:
					decstart=a
				retstr+=arg[a]
			elif hexstart!=None and string.hexdigits.find(arg[a].upper())>-1:
				retstr+=arg[a]
			elif (string.letters.find(arg[a])>-1 or arg[a]=='_') and stringstart==None:
				#var name here
				if varstart==None:
					varstart=a
					varend=None
			else:
				retstr+=arg[a]
		#for loop ended
		if stringstart!=None and stringend==None:
			raise SystemExit,'Missing '+stringstartchar+' on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
		elif varstart!=None and varend==None:
			if recurseLvl==0:
				varpart = arg[varstart:]
				varstart=None
				varend=len(arg)
				if self.prefixAuto==1:
					retstr,varpart = self.parsePrefixAuto(varpart, retstr)
				elif (self.prefixSphere==1 and varpart.lower().find('sphere.')!=0) or (self.prefixLocal==1 and varpart.lower().find('local.')==0):
					localRemoved=0
					if self.prefixLocal==1 and varpart.lower().find('local.')==0:
						varpart=varpart[6:]
						localRemoved=1
					#function call or local variable
					retstr = self.parseVariable(retstr, varpart,localRemoved,-1)
				else:
					#if (self.prefixSphere==1 and varpart.lower().find('sphere.')!=0) or (self.prefixLocal==1 and varpart.lower().find('local.')==0):
					sphereRemoved=0
					if self.prefixSphere==1 and varpart.lower().find('sphere.')==0:
						varpart=varpart[7:]
						sphereRemoved=1
					retstr = self.parseVariable(retstr, varpart,-1,sphereRemoved)
		#retstr=self.translateKnownArrayDefNames(retstr)				
		if retpos==None:
			return retstr
		else:
			return (retstr,retpos)

	def parsePrefixAuto(self, varpart, retstr=None):
		sphereRemoved=-1
		localRemoved=-1
		if varpart.lower().find('self.')==0:
			varpart=varpart[5:]
			localRemoved=0
		elif varpart.lower().find('src.')==0:
			localRemoved=0
		elif varpart.lower().find('act.')==0:
			localRemoved=0
		elif varpart.lower().find('link.')==0:
			localRemoved=0
		elif varpart.lower().find('region.')==0:
			localRemoved=0
		elif varpart.lower().find('multi.')==0:
			localRemoved=0
		elif varpart.lower().find('argo.')==0:
			localRemoved=0
		elif varpart.lower().find('serv.')==0:
			localRemoved=0
		elif varpart.lower().find('return')==0:
			localRemoved=0
		else:
			localRemoved=1
		if retstr!=None:
			retstr = self.parseVariable(retstr, varpart,localRemoved,sphereRemoved)
			return retstr,varpart
		else:
			return varpart

	def parseArgs(self, args, cstr, cmdargs, retstr):
		if len(args)>0:
			if self.supports[self.sphereVer]['functionParameters']:
				cstr+='('
			else:
				cstr+=' '
			iaa=0	
			firstArg=1
			for arg2 in args:
				arg2=arg2.strip()
				if not self.supports[self.sphereVer]['functionParameters'] and len(cmdargs)>iaa:
					arg3=arg2
					if self.prefixAuto==1:
						arg3 = self.parsePrefixAuto(arg2)
					elif self.prefixLocal==1 and arg2.lower().find('local.')==0:
						arg3=arg3[6:]
					retstr+='var.'+cmdargs[iaa].strip()+'='+arg3+'\n'
				else:
					if firstArg:
						firstArg=0
					else:
						if not self.supports[self.sphereVer]['functionParameters']:
							cstr+=' '
						else:
							cstr+=','
					tt=self.translateParam(arg2)
					if tt.__class__==tuple:
						tt=tt[0]
		
					cstr+=tt
				iaa+=1
				
			if self.supports[self.sphereVer]['functionParameters']:
				cstr+=')'
		return retstr, cstr
	
	def parseVariable(self,retstr, varpart,localRemoved,sphereRemoved):
		lparen = varpart.find('(')
		if lparen>-1:
			rparen = self.findn(varpart,')',lparen)
		else:
			rparen=-1
			#raise SystemExit,'Missing ) on line '+str(self.lineNum)+' of '+self.moduleName+'.py. (ParseVariable)'
		if lparen==-1 and rparen==-1:
			#variable
			if self.isKnownDefName(varpart) and self.defnameParse:
				retstr+=varpart
			else:
				retstr+=self.evalStartChar
				lbracket = varpart.find('[')
				if lbracket>-1:
					rbracket = self.findn(varpart, ']', lbracket)
				else:
					rbracket=-1
					#raise SystemExit,'Missing ] on line '+str(self.lineNum)+' of '+self.moduleName+'.py.'
				if lbracket==-1 and rbracket==-1:
					if localRemoved>-1:
						dot = varpart.find('.')
						if dot>-1:
							cstr=varpart[dot+1:]
							if localRemoved:
								retstr+=self.generateFindUid(varname='local.'+varpart[:dot],condition=cstr)
							else:
								retstr+=self.generateFindUid(varname=varpart[:dot],condition=cstr)
						else:
							#commented out code here is from R8-, new code R9+
							#retstr+=self.varheader()+varpart
							retstr+=self.generateLocalGet(varpart)
							
					else:
						retstr+=varpart
				elif lbracket!=-1 and rbracket!=-1:
					if localRemoved>-1:
						dot = varpart.find('.')
						if dot>-1:
							cstr=varpart[dot+1:lbracket]
							if localRemoved:
								retstr+=self.generateFindUid(varname='local.'+varpart[:dot],condition=cstr)
							else:
								retstr+=self.generateFindUid(varname=varpart[:dot],condition=cstr)
						else:
							#commented out code here is from R8-, new code R9+
							#retstr+=self.varheader()+varpart[:lbracket]
							retstr+=self.generateLocalGet(varpart[:lbracket])
							
					else:
						retstr+=varpart[:lbracket]
					tt=self.translateParam(varpart[lbracket+1:rbracket])
					if tt.__class__==tuple:
						tt=tt[0]
					retstr+='['+tt+']'
					retstr+=varpart[rbracket+1:]
				else:
					raise SystemExit,varpart+' on line '+str(self.lineNum)+' of '+self.moduleName+'.py has a missing bracket.'
				retstr+=self.evalEndChar
			
		else:
			#function
			if sphereRemoved>-1:
				cstr=self.evalStartChar
			if lparen==-1 or rparen==-1:
				raise SystemExit,varpart+' on line '+str(self.lineNum)+' of '+self.moduleName+'.py looks like it should be a function call, but it lacks ()s.'
			cmdline = varpart[:lparen]
			cmdargs = self.getArgs(cmdline)
			argtxt = varpart[lparen+1:rparen]
			after=varpart[rparen+1:]
			args = self.split(argtxt,',')
			if sphereRemoved>-1:
				cstr+=cmdline
				retstr = self.finish(args, cstr, cmdargs, retstr, after)
			else:
				lbracket = varpart.find('[')
				if lbracket>-1:
					rbracket = varpart.find(']', lbracket)
				else:
					rbracket = varpart.find(']')
				if lbracket==-1 and rbracket==-1:
					dot = cmdline.find('.')
					if dot>-1:
						cstr=cmdline[dot+1:]
						retstr, cstr = self.parseArgs(args, cstr, cmdargs, retstr)
						if localRemoved:
							retstr+=self.generateFindUid(varname='local.'+cmdline[:dot],condition=cstr)
						else:
							retstr+=self.generateFindUid(varname=cmdline[:dot],condition=cstr)
					else:
						#commented out code here is from R8-, new code R9+
						#retstr+=self.varheader()+cmdline
						retstr+=self.generateLocalGet(cmdline)
							
					retstr+=after
				elif lbracket!=-1 and rbracket!=-1:
					dot = cmdline.find('.')
					if dot>-1:
						cstr = cmdline[dot+1:lbracket]
						tt=self.translateParam(cmdline[lbracket+1:rbracket])
						if tt.__class__==tuple:
							tt=tt[0]
						
						cstr+='['+tt+']'
						cstr+=cmdline[rbracket+1:]
						retstr, cstr = self.parseArgs(args, cstr, cmdargs, retstr)
						if localRemoved:
							retstr+=self.generateFindUid(varname='local.'+cmdline[:dot],condition=cstr)
						else:
							retstr+=self.generateFindUid(varname=cmdline[:dot],condition=cstr)
						retstr+=after
					else:
						cstr=''
						cstr+=self.evalStartChar
						#commented out code here is from R8-, new code R9+
						#cstr+=self.varheader()+cmdline[:lbracket]
						cstr+=self.generateLocalGet(cmdline[:lbracket])
						tt=self.translateParam(cmdline[lbracket+1:rbracket])
						if tt.__class__==tuple:
							tt=tt[0]
						
						cstr+='['+tt+']'
						cstr+=cmdline[rbracket+1:]
						retstr = self.finish(args, cstr, cmdargs, retstr, after)
				else:
					raise SystemExit,cmdline+' on line '+str(self.lineNum)+' of '+self.moduleName+'.py has a missing bracket.'
		return retstr
		
	def finish(self, args, cstr, cmdargs, retstr, after):
		retstr, cstr = self.parseArgs(args, cstr, cmdargs, retstr)
		cstr+=after
		cstr+=self.evalEndChar
		retpos=len(retstr)
		retstr=retstr+cstr
		return retstr
	
	def generateBlock(self, what, varname=None, minval=None, maxval=None, arrayname=None, condition=None, noparseCondition=0):
		if self.produceReadableCode:
			sphereVer=self.sphereVer+'readable'
			try:
				test=self.patterns[sphereVer][what]
			except KeyError:
				sphereVer=self.sphereVer
		else:
			sphereVer=self.sphereVer
		block={}
		block['start'] = self.metaparse(self.patterns[sphereVer][what]['start'],varname, minval, maxval, arrayname, condition,noparseCondition=noparseCondition)
		block['end'] = self.metaparse(self.patterns[sphereVer][what]['end'],varname, minval, maxval, arrayname, condition,noparseCondition=noparseCondition)
		block['body_external'] = self.patterns[sphereVer][what]['body_external']
		block['external_start'] = self.metaparse(self.patterns[sphereVer][what]['external_start'],varname, minval, maxval, arrayname, condition,noparseCondition=noparseCondition)
		block['external_end'] = self.metaparse(self.patterns[sphereVer][what]['external_end'],varname, minval, maxval, arrayname, condition,noparseCondition=noparseCondition)
		self.blocks.append(block['end'])
		self.blockTab+=1
		bobe=0
		if block['start']!=None:
			self.scp_write(block['start'])
		if block['external_start']!=None:
			self.extraText.append(block['external_start'])
		if block['body_external']==1 and self.writeToExtraText==0:
			bobe=1
			self.writeToExtraText=1
		self.extraTextBlocks.append((block['external_end'],bobe))
				
	def generateFindUid(self, varname, condition):
		what='finduid'
		if self.produceReadableCode:
			sphereVer=self.sphereVer+'readable'
			try:
				test=self.patterns[sphereVer][what]
			except KeyError:
				sphereVer=self.sphereVer
		else:
			sphereVer=self.sphereVer
		minval=None
		maxval=None
		arrayname=None
		block={}
		block['start'] = self.metaparse(self.patterns[sphereVer][what]['start'],varname, minval, maxval, arrayname, condition, noparseCondition=1)
		return block['start']
	def metaparse(self, arg, varname=None, minval=None, maxval=None, arrayname=None, condition=None, noparseCondition=0, noparseVarname=0):
		if arg==None:
			return arg
		ltstart=[]
		skip=0
		retVal=''
		conversions={}
		conversions['c']=None
		conversions['m']=self.moduleName
		conversions['f']=self.functionName
		conversions['l']=str(self.lineNum)
		conversions['V']=None
		conversions['i']=None
		conversions['x']=None
		conversions['a']=None
		conversions['A']=None
		conversions['-']=None
		conversions['<']=None
		conversions['>']=None
		conversions['(']=None
		conversions[')']=None
		if varname!=None:
			if noparseVarname:
				conversions['v']=varname
			else:
				tt=self.translateParam(varname)
				if tt.__class__==tuple:
					tt=tt[0]
				conversions['v']=tt
				tt=self.translateParam(varname+'__val')
				if tt.__class__==tuple:
					tt=tt[0]
				conversions['V']=tt
		if condition!=None:
			if noparseCondition:
				conversions['c']=condition
			else:
				tt=self.translateParam(condition)
				if tt.__class__==tuple:
					tt=tt[0]
				conversions['c']=tt
		if minval!=None:
			tt=self.translateParam(minval)
			if tt.__class__==tuple:
				tt=tt[0]
			conversions['i']=tt
		if maxval!=None:
			tt=self.translateParam(maxval)
			if tt.__class__==tuple:
				tt=tt[0]
			conversions['x']=tt
		if arrayname!=None:
			tt=self.translateParam(arrayname)
			if tt.__class__==tuple:
				tt=tt[0]
			conversions['a']=tt
			if varname!=None:
				tt=self.translateParam(arrayname+'['+varname+'__val]')
				if tt.__class__==tuple:
					tt=tt[0]
				conversions['A']=tt
		
		for ch in range(0,len(arg)):
			if ch<len(arg)-1 and arg[ch]=='%':
				cv = conversions[arg[ch+1]]
				if cv!=None:
					retVal+=cv
					skip=2
			if skip==0:
				retVal+=arg[ch]
			else:
				skip-=1
		retVal=self.metaparseLTGT(retVal)
		retVal=self.metaparseLPGP(retVal)
		retVal=self.metaparsePD(retVal)
		return retVal
	
	def metaparsePD(self, arg):
		skip=0
		retVal=''
		for ch in range(0,len(arg)):
			if ch<len(arg)-1 and arg[ch]=='%':
				if arg[ch+1]=='-':
					if len(arg)>ch+5:
						if arg[ch+2:ch+6].lower()=='var.':
							skip=6
			if skip==0:
				retVal+=arg[ch]
			else:
				skip-=1
		return retVal
	
	def metaparseLPGP(self, arg):
		ltstart=[]
		skip=0
		retVal=''
		for ch in range(0,len(arg)):
			if ch<len(arg)-1 and arg[ch]=='%':
				if arg[ch+1]=='(':
					skip=2
				elif arg[ch+1]==')':
					if retVal[-1]==')':
						retVal=retVal[:-1]
					skip=2
							
			if skip==0 and len(ltstart)==0:
				retVal+=arg[ch]
			else:
				skip-=1
		return retVal
	
	def metaparseLTGT(self, arg):
		ltstart=[]
		skip=0
		retVal=''
		for ch in range(0,len(arg)):
			if ch<len(arg)-1 and arg[ch]=='%':
				if arg[ch+1]=='<':
					skip=2
					ltstart.append(ch+2)
				elif arg[ch+1]=='>':
					s=ltstart.pop()
					st=self.stripLTGT(arg[s:ch])
					if st[0]=='<':
						st=st[1:]
					if st[-1]=='>':
						st=st[:-1]
					retVal+=st
					skip=2
							
			if skip==0 and len(ltstart)==0:
				retVal+=arg[ch]
			else:
				skip-=1
		return retVal
	
	#varheader is deprecated. Use generateLocalSet and generateLocalGet instead.
	#This returns the 'header' that's put before the names of local variables to ensure there aren't 
	#name collisions between local vars in different functions, modules (files), etc.
	def varheader(self):
		if self.produceReadableCode:
			return 'var.'
		else:
			return 'var.py__'+self.moduleName+'__'+self.functionName+'__'
	
	# ARG(name, setvalue)
	def generateLocalSet(self, condition, varname, noparseVarname):
		what='localset'
		if self.produceReadableCode:
			sphereVer=self.sphereVer+'readable'
			try:
				test=self.patterns[sphereVer][what]
			except KeyError:
				sphereVer=self.sphereVer
		else:
			sphereVer=self.sphereVer
		minval=None
		maxval=None
		arrayname=None
		block={}
			
		block['start'] = self.metaparse(self.patterns[sphereVer][what]['start'],varname, minval, maxval, arrayname, condition, noparseCondition=1, noparseVarname=noparseVarname)
		return block['start']	
	
	def generateLocalGet(self, condition):
		what='local'
		if self.produceReadableCode:
			sphereVer=self.sphereVer+'readable'
			try:
				test=self.patterns[sphereVer][what]
			except KeyError:
				sphereVer=self.sphereVer
		else:
			sphereVer=self.sphereVer
		varname=None
		minval=None
		maxval=None
		arrayname=None
		block={}
		block['start'] = self.metaparse(self.patterns[sphereVer][what]['start'],varname, minval, maxval, arrayname, condition, noparseCondition=1)
		return block['start']	

def hasContent(line):
	for a in line:
		if a!=' ' and a!='\t':
			return 1
	return 0

#The first thing run! Calls main(). Lucky you, you don't need anything like this in your PySphere scripts. :P
if __name__ == '__main__': main()
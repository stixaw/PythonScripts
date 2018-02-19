# Copy msi to ali-netapp1

import fnmatch
import getopt
import os
import shutil
import sys
from os.path import join, abspath
import time
import win32wnet
import datetime
import tempfile
import logging
import threading


#global variables
TIM_STMP=''
Bld_Dir = ''
Sol_Dir = ''
Src_Dir = ''
SolName = ''
FirstRun = False
Version = ''
BuildBasePath = ''
top =''

def usage():
	print __doc__
	print """Usage:
	Msi_copy.py [OPTIONS]
	Options:
	"""
	usage ="""\
	-h, --help|display help
	--solution|Solution Initials, example --solution=DS or -s=AM
	--srcdir|Locaition to find MSI example --srcdir=c:\output_msi
	--firstrun | this specifies to create the base Bld_Dir example --firstrun
	--buildnum | this is the itsmversion number 7.1.xxx.0 Version global variable
	--top|%workspace% is needed to run signing functions
  """

def parseArgs(argv):
	global FirstRun, SolName, Src_Dir, Version, top
	try:
		opts, args = getopt.getopt(argv, "hf:s:s:b:t", [ 'help', 'firstrun', 'solution=', 'srcdir=', 'buildnum=', 'top=' ])
	except getopt.GetoptError:
		print "Invalid options specified.\n"
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		if opt ==("--firstrun"):
			FirstRun = True
		elif opt == ("--solution"):
			SolName = arg
		elif opt == ('--srcdir'):
			Src_Dir = arg
		elif opt == ('--buildnum'):
			Version = arg
		elif opt == ('--top'):
			top = arg

	if SolName == '':
		print 'You must specify --solution|Solution Initials, example --solution=DS'
		sys.exit(3)
	if Src_Dir == '':
		print 'You must specify --srcdir|Locaition to find MSI example --srcdir=c:\output_msi'
		sys.exit(4)
	if Version =='':
		print 'You must specify --buildnum example --buildnum=7.1.1356'
		sys.exit(5)
	if top =='':
		print 'You must speicify --top=%WORKSPACE%'
		sys.exit(6)
	if FirstRun:
		if Version =='':
			print 'You must specify --buildnum when using FirstRun, example --buildnum=7.1.1356, FirstRun always creates the Time stamp directory'
			sys.exit(7)

class BuildError(Exception):
	def __init__(self, msg, *args):
		Exception.__init__(self, msg)
		self.msg = msg
		#apply(Exception.__init, (self,) + args)
def fail(msg):
	print '%s failed: %s' % (sys.argv[0], msg)
	sys.exit(1)
 
try:
	# set globals from the command line
	parseArgs(sys.argv[1:])
	
	#Build Dir for MSI Copy
	Dst_Path =  '\\\\ali-netapp1.altiris.com\\polaris\\ITMS\\CombinedBuild\\Daily_Builds'

except BuildError, e:
	fail(e.msg)

def GetTime():
	global TIM_STMP
	TIM_STMP = time.strftime("%Y%m%d%H%M", time.gmtime())
	print TIM_STMP
	return TIM_STMP

def Execute(dir, cmd, reportFail=1):
	"""execute a command from a given directory"""
	if sys.platform == 'win32':
		tmpfile = tempfile.mkstemp(suffix='.bat', text=True)
		tmphandle = tmpfile[0]
		tmpname = tmpfile[1]

		os.write(tmphandle, '@echo off\n')
		if dir != '':
			os.write(tmphandle, 'cd %s\n' % dir)
		os.write(tmphandle, '%s\n' % cmd)
		os.close(tmphandle)

		result = os.system(tmpname)
		os.remove(tmpname)
		if result != 0:
			if reportFail:
				raise BuildError('Executing %s from direction %s failed' % (cmd, dir))

def SignFiles(pwd, dir):
	global top
	privateKey = top + '\\CM\\Verisign\\mycredentials.pfx'
	signingToolsDir = top + r'\CM\Verisign'
	sign_tool = top + r'\CM\Verisign\signtool.exe'

	# Put the password into the registry.  -s supresses the prompt.
	#dopswdregPath = signingToolsDir + '\\dopswd.reg'
	#f = open(dopswdregPath, 'w')
	#f.write('ITMSCMDS')
	#f.close()

	#cmd=('regedit /C /S ' + dopswdregPath)
	#print cmd
	#Execute(signingToolsDir , cmd)

	for msi in os.listdir(dir):
		if fnmatch.fnmatch(msi, '*.msi'):
			msitosign = os.path.join(dir, msi)
			print msitosign
			#filename = os.path.basename(msitosign)
			#print filename
			#D:\WORKSPACE\Signtool>signtool.exe sign /f mycredentials.pfx /p ITMSCMDS /t http://timestamp.verisign.com/scripts/timstamp.dll Altiris_DeploymentSolutionLanguages_x64.msi
			cmd1 = sign_tool + ' sign /f ' + privateKey +' /p ' + pwd + ' /t http://timestamp.verisign.com/scripts/timstamp.dll ' + msitosign
			#cmd = signingToolsDir + '\\DoPswd.exe signcode -C ' + top + '\\CM\\Verisign\\SignCode.exe -spc ' + top + '\\CM\\Verisign\\mycredentials.spc -v ' + privateKey + ' -a SHA1 -t http://timestamp.verisign.com/scripts/timstamp.dll ' + msitosign + ' -n "' + filename + '"'
			print 'Running "' + cmd1 + '"...'
			Execute (top, cmd1)  
		else:
			logging.error('Error while signing ' + msi)

def MakeBaseDir():
	global Version, BuildBasePath
	if FirstRun:
		print Version
		BuildBasePath = Dst_Path + '\\' + Version
		if os.path.exists(BuildBasePath):
			print "Directory ", BuildBasePath, " already exists"
		if not os.path.exists(BuildBasePath):
			print "Creating ", BuildBasePath
			os.makedirs(BuildBasePath)
	else:
		print Version
		BuildBasePath = Dst_Path + '\\' + Version
		print BuildBasePath
		return BuildBasePath

def wnet_connect(host, username = None, password = None):
	netpath = r'\\ali-netapp1.altiris.com\polaris'
	networkPath = netpath
	unc = ''.join(['\\\\', host])
	print unc
	try:
		win32wnet.WNetAddConnection2(0, None, unc, None, username, password)
	except Exception, err:
		if isinstance(err, win32wnet.error):
			#Disconnect previous connections if detected, and reconnect.
			if err[0] == 1219:
				win32wnet.WNetCancelConnection2(unc, 0, 0)
				return wnet_connect(host, username, password)
		raise err

def MakeBldDir():
	global Bld_Dir, BuildBasePath
	Bld_Dir = (BuildBasePath + '\\%s' % (TIM_STMP))
	#create the directory for Solution
	if not os.path.exists(Bld_Dir):
		print "Creating ", Bld_Dir
		os.makedirs(Bld_Dir)
	return Bld_Dir

def MakeSolDir(Name):
	global  Bld_Dir, Sol_Dir, SolName
	print Bld_Dir
	print SolName
	Sol_Dir = Bld_Dir + '\\' + SolName
	print Sol_Dir
	if not os.path.exists(Sol_Dir):
		print "Creating ", Sol_Dir
		os.makedirs(Sol_Dir)

def CopyMSI(Src_Dir):
	global Sol_Dir
	#copy the msi to ali-netapp solution directory
	for file in os.listdir(Src_Dir):
		if fnmatch.fnmatch(file, '*.msi'):
			dirfile = os.path.join(Src_Dir, file)
			print "Copying ", dirfile, "to ", Sol_Dir
			shutil.copy(dirfile, Sol_Dir)

def GetBldDir():
	global Dst_Path, Bld_Dir, BuildBasePath
	print BuildBasePath
	highdir = max([int(x) for x in os.listdir(BuildBasePath) if x.isdigit()])
	Bld_Dir  = BuildBasePath + "\\" + str(highdir)
	print "the Build Directory for this run is ", Bld_Dir

#This is the main program
if __name__ == '__main__':
	try:
		if FirstRun:
			SignFiles('ITMSCMDS','C:\\output_msi')
			wnet_connect('ali-netapp1.altiris.com', username = 'altiris' + '\\' + 'srvc_aexns_dev', password = 'SRVC_AeXNS_Dev')
			GetTime()
			MakeBaseDir()
			MakeBldDir()
			MakeSolDir(SolName)
			CopyMSI(Src_Dir)
		else:
			SignFiles('ITMSCMDS', 'C:\\output_msi')
			wnet_connect('ali-netapp1.altiris.com', username = 'altiris' + '\\' + 'srvc_aexns_dev', password = 'SRVC_AeXNS_Dev')
			MakeBaseDir()
			GetBldDir()
			MakeSolDir(SolName)
			CopyMSI(Src_Dir)
	except BuildError, e:
		fail(e.msg)

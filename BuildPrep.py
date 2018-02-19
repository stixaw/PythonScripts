#this script calls the gather scripts
#checks out the files needed for a build
# Calls build.py with a --nosign, will be manual build which is no label and just for testing purposes.
#randomly generates a --buildnum so if two developers are building manual builds on their machines they will not overwrite on the copy command to builddev

import getopt
import os
import shutil
import sys
from indent import *
import glob
import zipfile
import random

#ugly global variables:
rnum = ''
want = ''
have =''
StagingPath = ''
version = 'latest'
DPT_TRNK = '//depot/Endpoint_Management_Group/notification_server/solutions/deployment_solution/top...'
top = ''
workspace = ''
submit = False
All = False
BDC = False
RD = False
SBS = False
GPL = False
CFG = False


#this is for help function to build a commandline
def usage():
  print __doc__
  print """Usage:
StagingGather.py [OPTIONS]

Options:
"""
  usage = """\
Required Parameters|These are required to run this script --path, --top and possible -user and -pass
--path|path to Drive you want to use for a local distrib by example --path=c:
--top|path to top or top example --top=c:\ds\trunk
--buildnum|if a developer wants to specify the number for the test build example --buildnum=999
--workspace|provide the workspace to be used for the local build
Optional input parameters|By default this script will gather all possible Staging files BDC, RD, SBS, GPL, nogather, nosubmit
--nogather|Turns off the gather function for preboot files from Rdbuild/Builddev
--revert|you will revert the distrib files in source after the practise build
--bdc|gather only bootwiz tree to staging then execute build.bat sn command
--rd|gather only rdeploy files to staging
--sbs|gather only SBS tree to staging
--gpl|gather BDCgpl_6.9.XXX.frm and rename to BDCfrm.gpl file
--cfg|gather, aclient-config*.dll and rename to config.dll
--version|Designates a specific version set to latest by default example Rdbuild: --version=9598 builddev: --version=build447
you must have a file called workspace.txt with your designated workspace on the system you are running a local build on for the gather
example commandline Buildprep.py --path=c: --top=c:\ds\trunk
--help|display help

"""
  rows = [row.strip().split('|') for row in usage.splitlines()]
  print (rows, delim='  ', wrapfunc=lambda x: wrap_onspace_strict(x, 40))

def parseArgs(argv):
  global StagingPath, All, BDC, RD, SBS, GPL, CFG, version, top, submit, workspace

  try:
    opts, args = getopt.getopt(argv, 'hbrsgcnw:v:p:t', ['help', 'bdc',
      'rd', 'sbs', 'gpl', 'cfg', 'nogather','workspace=','version=','path=', 'top='])
  except getopt.GetoptError:
    print "Invalid options specified.\n"
    usage()
    sys.exit(2)

  for opt, arg, in opts:
    if opt in ('--help'):
      print "HELP"
      usage()
      sys.exit()
    elif opt in ('--path'):
      StagingPath = arg
      print "I am using this drive", StagingPath, "for distrib staging area"
	elif opt in ('--top'):
      top = arg
      print "Local trunk for p4 commands and copy of zip file to distrib to prepare for build =", top
	elif opt in ('--nogather'):
      All = False
      print "Calling all current gather functions, SBS, BDC, Rdeploy, LinuxGpl, and Config.dll"
    elif opt in ('--bdc'):
      All = False
      BDC = True
      print "Gathering Bootwiz from rdbuild only"
    elif opt in ('--rd'):
      All = False
      RD = True
      print "Gathering rdeploy from rdbuild only"
    elif opt in ('--sbs'):
      All = False
      SBS = True
      print "Gathering SBS from rdbuild only"
    elif opt in ('--gpl'):
      All = False
      GPL = True
      print "Gathering Linux_gpl from rdbuild only"
    elif opt in ('--cfg'):
      All = False
      CFG = True
      print "Gathering config.dll from builddev only"
    elif opt in ('--buildnum'):
      rnum = arg
      print "Specified Buildnumber for this test build=", buildnum
    elif opt in ('--version'):
      version = arg
      print "Specified version of gather files", version
  if workspace == '':
    print 'You must specify local workspace for p4 commands to work, example --workspace=angel-ds'
    sys.exit(4)
  if top == '':
    print 'You must specify local workspace trunk path, example --top=<c:\ds\trunk>'
    sys.exit(4)
  if StagingPath == '':
    print 'You must specify --path=<Staging path>'
    sys.exit(4)
	
class BuildError(Exception):
  def __init__(self, msg, *args):
    Exception.__init__(self, msg)
    self.msg = msg
    #apply(Exception.__init, (self,) + args)
try:
  # set globals from the command line
  parseArgs(sys.argv[1:])

def GetBuildNumber():
  global buildnum
  if rnum =='':
    print "generating random buildnumber"
 #produces a random build number for the command --buildnum
    rnum = random.randrange(900, 1000) -1
	print rnum
  else:
    print "using", rnum



def RunBuildPy():
  global top, rnum
#calling build.py to run the no label manual build
  command = 'python ' + top + '\\build\\scripts\\build.py ' +'--top='+ top + ' --version=7.1. --buildnum=%d --nosign' % (rnum)
  print 'CALLING', command

def CleanBuildPy():
#calling build.py to clean up all binaries and distrib extracted zip files
  command = 'python ' + top + '\\build\\scripts\\build.py ' +'--top='+ top + ' --cleanall'

def CallGather():
#this function calls all gather scripts with correct parameters for all gather

  
def RemoveFile(path):
  if os.path.exists(path):
    os.remove(path)



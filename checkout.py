#p4 checkout files for local build (dev test build)
#this will either checks out the files
#To make a full build you would normally check out these files (perforce)
#trunk\apps\DeploymentClient\Install\*.wsi (all the wsi files there)
#trunk\apps\DeploymentServer\install\*.wsi (all the wsi files there)
#trunk\apps\DeploymentServer\Deployment\Config\Altiris.Deployment_Collections.config
#trunk\apps\DeploymentInstall\*.wsi (all the wsi files there)
#trunk\distrib\bootwiz (the entire directory)
#trunk\distrib\config\config.dll
#and then revert them if you provide the revert switch

import getopt
import os
import shutil
import sys
from indent import *
import glob

#ugly global variables
DPT_TRNK = '//depot/Endpoint_Management_Group/notification_server/solutions/deployment_solution/trunk...'
checkout = ''
revert = ''
workspace = ''
user = ''

#this is for help function to build a commandline
def usage():
  print __doc__
  print """Usage:
checkout.py [OPTIONS]

Options:
"""
  usage = """\
Required Parameters|These are required to run this script --path, --trunk and possible -user and -pass
--checkout|checks out from perforce all files modified by local build process
--revert|reverts all files post build that were modified by local build process
--workspace|provides local workspace for p4 -c option
--user|provides username for p4 access to depot
--help|display help
"""
  rows = [row.strip().split('|') for row in usage.splitlines()]
  print indent(rows, delim='  ', wrapfunc=lambda x: wrap_onspace_strict(x, 40))

def parseArgs(argv):
  global checkout, revert, workspace, user

  try:
    opts, args = getopt.getopt(argv, 'hcvw:u', ['help', 'checkout', 'revert', 'workspace=', 'user=',])
  except getopt.GetoptError:
    print "Invalid options specified.\n"
    usage()
    sys.exit(2)

  for opt, arg, in opts:
    if opt in ('--help'):
      print "HELP"
      usage()
      sys.exit()
    elif opt in ('--workspace'):
      workspace = arg
    elif opt in ('--user'):
      user = arg
    elif opt in ('--checkout'):
      revert = False
      checkout = True
      print "checking out files modified during a build"
    elif opt in ('--revert'):
      checkout = False
      revert = True
      print "Reverting files modified during a build"
  if workspace == '':
   print 'You must specify a workspace example --workspace= angel-ds'
   sys.exit(4)

  if user == '':
    print 'You must specify a user example --user= angel_smith'
    sys.exit(4)

class BuildError(Exception):
  def __init__(self, msg, *args):
    Exception.__init__(self, msg)
    self.msg = msg
    #apply(Exception.__init, (self,) + args)
try:
  # set globals from the command line
  parseArgs(sys.argv[1:])

  BUILD_FILES = [
    DPT_TRNK + r'/apps/DeploymentClient/install/Altiris_Deployment_Agent.wsi',
    DPT_TRNK + r'/apps/DeploymentClient/install/Altiris_Deployment_Agent_x64.wsi',
    DPT_TRNK + r'/apps/DeploymentInstall/Altiris_Deployment.wsi',
    DPT_TRNK + r'/apps/DeploymentInstall/Altiris_Deployment_x64.wsi',
    DPT_TRNK + r'/apps/DeploymentInstall/Altiris_NS_DriversDB.wsi',
    DPT_TRNK + r'/apps/DeploymentInstall/altiris_ns_linux_gpl.wsi',
    DPT_TRNK + r'/apps/DeploymentInstall/altiris_ns_winpe2.1.wsi',
    DPT_TRNK + r'/apps/DeploymentInstall/altiris_ns_winpe2.1_x64.wsi',
    DPT_TRNK + r'/apps/DeploymentServer/Deployment/Config/Altiris.Deployment_Collections.config',
    DPT_TRNK + r'/apps/DeploymentServer/install/Altiris_Deployment_TaskServerHandler.wsi',
    DPT_TRNK + r'/apps/DeploymentServer/install/Altiris_Deployment_TaskServerHandler_x64.wsi',
    DPT_TRNK + r'/distrib/DSPortal/DSPortal.xap',
    DPT_TRNK + r'/distrib/config.zip',
    DPT_TRNK + r'/distrib/rdeploy.zip',
    DPT_TRNK + r'/distrib/SBS.zip',
    DPT_TRNK + r'/distrib/bootwiz.zip',
    DPT_TRNK + r'/distrib/linuxgpl.zip'   
    ]
except BuildError, e:
  fail(e.msg)

def P4vSync():
  global workspace, user
  #sync up the workspace with depot
  os.system("p4 -u %s -c %s sync %s" % (user, workspace, DPT_TRNK))

def P4vCheckout():
  global workspace
#checkout files modifed in build process
  for f in BUILD_FILES:
    os.system("p4 -u %s -c %s edit %s" % (user, workspace, f)) 

def P4vRevert():
  global workspace, user
# rever files modified by build procses
  for f in BUILD_FILES:
    os.system("p4 -u %s -c %s revert %s" % (user, workspace, f))

## MAIN
if __name__ == '__main__':

  try:
    if checkout == True:
      P4vCheckout()
      P4vSync()
    else:
      P4vRevert()

  except BuildError, e:
    fail(e.msg)
#Staging Gather.py SUDO CODE to turn to real code
#This py is built to gather the binaries from external build source rdbuild\builds\trunk, Linuxbuild machine, PCTbuilds, ghost builds,
# Config.dll and driver db from Deployment server win32 builds (builddev.altiris.com\buildtest\....
#To staging area, so when prepare for build or build.py is called the files are available for the MSI

import getopt
import os
import shutil
import sys
from indent import *
import glob

#ugly global variables:
StagingPath = ''
All = True
BDC = False
RD = False
SBS = False
GPL = False
CFG = False
version = 'latest'
#GHT = False (need working source)
#LIN = False
#DDB =FALSE
#PCT =FALSE

#this is for help function to build a commandline
def usage():
  print __doc__
  print """Usage:
StagingGather.py [OPTIONS]

Options:
"""
  usage = """\
--path|path to Drive you want to use for a local distrib by example --path=c:
--trunk|path to localtrunk example --trunk=c:\ds\trunk
Optional input parameters|By default this script will gather all possible Staging files BDC, RD, SBS, GPL, nogather
--nogather
--bdc|gather only bootwiz tree to staging then execute build.bat sn command
--rd|gather only rdeploy files to staging
--sbs|gather only SBS tree to staging
--gpl|gather BDCgpl_6.9.XXX.frm and rename to BDCfrm.gpl file
--cfg|gather, aclient-config*.dll and rename to config.dll
--version|Designates a specific version set to latest by default example --version=598
--help|display help

"""
  rows = [row.strip().split('|') for row in usage.splitlines()]
  print indent(rows, delim='  ', wrapfunc=lambda x: wrap_onspace_strict(x, 40))

def parseArgs(argv):
  global StagingPath, All, BDC, RD, SBS, GPL, version, CFG, nogather

  try:
    opts, args = getopt.getopt(argv, 'habrsgc:s:p:', ['help','All', 'bdc',
      'rd', 'sbs', 'gpl', 'cfg', 'version=','path=',])
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
      print StagingPath
    elif opt in ('--bdc'):
      All = False
      BDC = True
      print 'BDC =',BDC
      print 'All =',All
    elif opt in ('--rd'):
      All = False
      RD = True
      print 'RD =',RD
      print 'All =',All
    elif opt in ('--sbs'):
      All = False
      SBS = True
      print 'SBS =',SBS
      print 'All =',All
    elif opt in ('--gpl'):
      All = False
      GPL = True
      print 'GPL =',GPL
      print 'All =',All
    elif opt in ('--cfg'):
      All = False
      CFG = True
      print 'CFG =',CFG
      print 'All =',All
    elif opt in ('--version'):
      version = arg

  if StagingPath == '':
    print 'You must specify --path=<Staging path>'
    sys.exit(4)

# def GetBuildNum(dirname):
 #better way to determine highest build to accommodate build447, 9226, 7.1.1001
    # return int('0' + ''.join([x for x in dirname if x.isdigit()]))
	# highestBuild = max([GetBuildNum(x) for x in os.listdir('C:\\TEST')])


class BuildError(Exception):
  def __init__(self, msg, *args):
    Exception.__init__(self, msg)
    self.msg = msg
    #apply(Exception.__init, (self,) + args)
try:
  # set globals from the command line
  parseArgs(sys.argv[1:])
	
# list of Source directories
  BDC_SRC = r'\\rdbuild.altiris.com\builds\trunk\%s\bootwiz\bootwiz' % version
  BDC_LOC_SRC = r'\\builddev.altiris.com\buildtest\Uinta\Bootwiz\Latest\ProgramFiles\Bootwiz'
  RD_LOC_SRC = r'\\builddev.altiris.com\buildtest\Uinta\RapiDeploy\Latest\ProgramFiles'
  RD_SRC =  r'\\rdbuild.altiris.com\builds\trunk\%s' % version
  SBS_SRC = r'\\rdbuild.altiris.com\builds\trunk\%s\PXE\SBS' % version
  GPL_SRC = r'\\rdbuild.altiris.com\builds\trunk\%s\bootwiz' % version
  # GHT_SRC = r'\\builddev.altiris.com\buildtest\Uinta\DeploymentServer\Build430-DS69sp3\ProgramFiles\Ghost'
  CFG_SRC = r'\\builddev.altiris.com\buildtest\Uinta\Dagent\Latest\ProgramFiles\Agents\AClient'
  # PCT_SCR = r'\\builddev.altiris.com\buildtest\Uinta\PCTransplantPro\v6.8\ + version'
  # DDB_SRC = r'\\builddev.altiris.com\buildtest\Uinta\DeploymentServer\Build430-DS69sp3\ProgramFiles\DriversDB'
  # LIN_SRC = r'\\<LINBUILD\Path\output_lin\

# List of destination directories
  BDC_DST = StagingPath + '\\bootwiz'
  RD_DST = StagingPath + '\\Imaging\\rdeploy\\'
  RD_x86_DST = StagingPath + '\\Imaging\\rdeploy\\x86\\'
  RD_64_DST = RD_DST + '\\x64\\'
  RD_LIN_DST = RD_DST + '\\Linux\\x86\\'
  RD_LIN_64_DST = RD_DST + '\\Linux\\x64\\'
  SBS_DST = StagingPath + '\\SBS\\'
  GPL_DST = StagingPath + '\\Linux_gpl\\'
  # GHT_DST = StagingPath + '\\Imaging\\ghost\\'
  # GHT_64_DST = GHT_DST + '\\x64\'\
  CFG_DST = StagingPath + '\\config\\' #rem this out once we make MSI Changes
  CFG_86_DST = StagingPath + '\\config\\x86\\'
  CFG_64_DST = StagingPath + '\\config\\x64\\'
  # PCT_DST = StagingPath + '\\PCT\\'
  # DDB_DST = r'StagingPath + \DriversDatabase\DriversDB\'
  # LIN_DST = r'StagingPath + \LIN_OUTPUT'

  RD_FILES = [
    RD_SRC + '\\tools\\Windows\\x86\\atrsimg.dll',
    RD_SRC + '\\rd\\RDeploy\\Windows\\imgexpl.exe',
    RD_SRC + '\\rd\\RDeploy\\Windows\\rdeploy.exe',
    RD_SRC + '\\rd\\RDeploy\\Windows\\rdeployt.exe',
    RD_SRC + '\\rd\\RDeploy\\Windows\\firm.exe',
    RD_SRC + '\\rd\\TechSup\\Windows\\partgen.exe',
    RD_SRC + '\\rd\\TechSup\\Windows\\showdisk.exe',
    RD_SRC + '\\rd\\TechSup\\Windows\\wipe.exe',
    RD_SRC + '\\rd\\TechSup\\Windows\\fscs.exe',
    RD_SRC + '\\rd\\TechSup\\Windows\\makeimx.exe'
    ]

  RD_X64_FILES = [
    RD_SRC + r'\tools\Windows\x64\atrsimg.dll',
    RD_SRC + r'\rd\RDeploy\Windows\x64\rdeploy.exe',
    RD_SRC + r'\rd\RDeploy\Windows\x64\rdeployt.exe',
    RD_SRC + r'\rd\RDeploy\Windows\x64\firm.exe',
    RD_SRC + r'\rd\TechSup\Windows\x64\partgen.exe',
    RD_SRC + r'\rd\TechSup\Windows\x64\showdisk.exe',
    RD_SRC + r'\rd\TechSup\Windows\x64\wipe.exe',
    RD_SRC + r'\rd\TechSup\Windows\x64\fscs.exe',
    RD_SRC + r'\rd\TechSup\Windows\x64\makeimx.exe'
    ]

  RD_LIN_FILES = [
    RD_SRC + r'\rd\RDeploy\Linux\rdeployt.',
    RD_SRC + r'\rd\RDeploy\Linux\firm.',
    RD_SRC + r'\rd\TechSup\Linux\fscs.',
    RD_SRC + r'\rd\TechSup\Linux\makeimx.',
    RD_SRC + r'\rd\TechSup\Linux\partgen.',
    RD_SRC + r'\rd\TechSup\Linux\showdisk.',
    RD_SRC + r'\rd\TechSup\Linux\wipe.'
    ]

  RD_X64_LIN_FILES = [
    RD_SRC + r'\rd\RDeploy\Linux\x64\rdeployt.',
    RD_SRC + r'\rd\RDeploy\Linux\x64\firm.',
    RD_SRC + r'\rd\TechSup\Linux\x64\fscs.',
    RD_SRC + r'\rd\TechSup\Linux\x64\makeimx.',
    RD_SRC + r'\rd\TechSup\Linux\x64\partgen.',
    RD_SRC + r'\rd\TechSup\Linux\x64\showdisk.',
    RD_SRC + r'\rd\TechSup\Linux\x64\wipe.'
    ]

#  BDC_LOC_FILES = [
#    BDC_LOC_SRC + '\\BootWiz_DE.dll',
#    BDC_LOC_SRC + '\\BootWiz_EN.dll',
#    BDC_LOC_SRC + '\\BootWiz_ES.dll',
#    BDC_LOC_SRC + '\\BootWiz_FR.dll',
#    BDC_LOC_SRC + '\\BootWiz_IT.dll',
#    BDC_LOC_SRC + '\\BootWiz_JP.dll',
#    BDC_LOC_SRC + '\\BootWiz_PT.dll',
#    BDC_LOC_SRC + '\\BootWiz_RU.dll',
#    BDC_LOC_SRC + '\\BootWiz_ZH.dll'
#    ]

#  RD_LOC_FILES = [
#    RD_LOC_SRC + '\\imgexpl_DE.dll',
#    RD_LOC_SRC + '\\imgexpl_en.dll',
#    RD_LOC_SRC + '\\imgexpl_ES.dll',
#    RD_LOC_SRC + '\\imgexpl_FR.dll',
#    RD_LOC_SRC + '\\imgexpl_IT.dll',
#    RD_LOC_SRC + '\\imgexpl_JP.dll',
#    RD_LOC_SRC + '\\imgexpl_PT.dll',
#    RD_LOC_SRC + '\\imgexpl_RU.dll',
#    RD_LOC_SRC + '\\imgexpl_zh.dll'
#    ]

except BuildError, e:
  fail(e.msg)

# is this possible? Build the DestDir Based on Parameter BDC, RD, SBS,  GPL, GHT, CONFIG, PCT, LIN,  
#def DestDir()

def CopyRD():
#copy x86 windows version of rdeploy files
  print "copying RD files from", RD_SRC
  if not os.path.exists(RD_DST):
    os.makedirs(RD_DST)
  if not os.path.exists(RD_x86_DST):
    os.makedirs(RD_x86_DST)
  for file in RD_FILES:
    print "copying rd files"
    shutil.copy(file, RD_DST)
    shutil.copy(file, RD_x86_DST)

#copy x86 windows version of imgexp localized files
  print "copying imgexp localized  from", RD_LOC_SRC
  for file in glob.glob(RD_LOC_SRC + r'\imgexpl_*.dll'):
    print "copying imgexp localized files"
    shutil.copy(file, RD_DST)
    shutil.copy(file, RD_x86_DST)

#copy the x64 windows version of rdeploy
  if not os.path.exists(RD_64_DST):
    os.makedirs(RD_64_DST)
  for file in RD_X64_FILES:
    print "copying rd_64 files"
    shutil.copy(file, RD_64_DST)

#copy the x86 linux version of rdeploy files
  if not os.path.exists(RD_LIN_DST):
    os.makedirs(RD_LIN_DST)
  for file in RD_LIN_FILES:
    print "copying rd_lin files"
    shutil.copy(file, RD_LIN_DST)

#copy the x64 linux version of rdeploy files
  if not os.path.exists(RD_LIN_64_DST):
    os.makedirs(RD_LIN_64_DST)
  for file in RD_X64_LIN_FILES:
    print "copying rd_lin_64 files"
    shutil.copy(file, RD_LIN_64_DST)

def CopyCFG():
# create directories if they don't exist
  print "copying x86 Config.dll files from", CFG_SRC
  if not os.path.exists(CFG_DST):
    os.makedirs(CFG_DST)
  if not os.path.exists(CFG_86_DST):
    os.makedirs(CFG_86_DST)
#delete the existing config.dll
  if os.path.exists(CFG_DST + '\\config.dll'):
    os.remove(CFG_DST + '\\config.dll')
  if os.path.exists(CFG_86_DST + '\\config.dll'):
    os.remove(CFG_86_DST + '\\config.dll')
#copy the x86 CFG file
  for file in glob.glob(CFG_SRC + r'\altiris-config-*.X86.dll'):
    print "copy config.dll file"
    shutil.copy(file, CFG_DST)
    shutil.copy(file, CFG_86_DST)
#rename "altiris-config-*.X86.dll"
  for name in glob.glob(CFG_DST + '\\altiris-config-*.X86.dll'):
    os.rename(name, CFG_DST + '\\config.dll')
  for name in glob.glob(CFG_86_DST + '\\altiris-config-*.X86.dll'):
    os.rename(name, CFG_86_DST + '\\config.dll')
#create x64 CFG file path
  if not os.path.exists(CFG_64_DST):
    os.makedirs(CFG_64_DST)
#delete x64 dll if it exists
  if os.path.exists(CFG_64_DST + '\\config.dll'):
    os.remove(CFG_64_DST + '\\config.dll')
  for file in glob.glob(CFG_SRC + r'\altiris-config-*.X64.dll'):
    print "copy  x64 config.dll file"
    shutil.copy(file, CFG_64_DST)
#rename "altiris-config-*.X86.dll"
  for name in glob.glob(CFG_64_DST + '\\altiris-config-*.X64.dll'):
    os.rename(name, CFG_64_DST + '\\config.dll')


#copy and rename BDCgpl_6.9.XXXX.frm
def CopyGPL():
  print "copying GPL files from", GPL_SRC
  if not os.path.exists(GPL_DST):
    os.makedirs(GPL_DST)
#if exist "%DST_DIR%\Linux_gpl\BdcGpl.frm" del "%DST_DIR%\Linux_gpl\BdcGpl.frm"
  if os.path.exists(GPL_DST + '\\BdcGpl.frm'):
    os.remove(GPL_DST + '\\BdcGpl.frm')
#copy the gpl file
  for file in glob.glob(GPL_SRC + r'\*.frm'):
    print "copy gpl.frm file"
    shutil.copy(file, GPL_DST)
#rename "%DST_DIR%\Linux_gpl\*.frm" BdcGpl.frm this can be removed according to nitin if we want to just keep the version # in name
  # for name in glob.glob(GPL_DST + '\\*.frm'):
    # os.rename(name, GPL_DST + '\\BDCgpl.frm')
 

# bootwiz tree command because we get all *.* including structure
def CopyBDC():
  print "copying BDC files from", BDC_SRC
  if os.path.exists(BDC_DST):
    shutil.rmtree(BDC_DST)
  print "copying BDC directory"
  shutil.copytree(BDC_SRC, BDC_DST)
#CD %DST_DIR%\bootwiz and call the build.bat to finalize the bootwiz for DS consumption
  print "Calling build.bat NS"
  os.chdir(BDC_DST)
  os.system('build.bat NS')
  os.remove('build.bat')

 for file in glob.glob(BDC_LOC_SRC + r'\BootWiz_*.dll')::
    print "copying localized BDC files"
    shutil.copy(file, BDC_DST)

# SBS tree command because we get all *.* including structure
def CopySBS():
  print "copying SBS files from", SBS_SRC
  if os.path.exists(SBS_DST):
    shutil.rmtree(SBS_DST)
#copy the directory of SBS to local staging
  print "Copying SBS directory"
  shutil.copytree(SBS_SRC, SBS_DST)

#define a copy all function
def CopyAll():
  CopyBDC()
  CopyRD()
  CopySBS()
  CopyGPL()
  CopyCFG()
  
#This is the main program
if __name__ == '__main__':
  print "All =", All
  try:
    if All:
      print "I am copying all"
      CopyAll()
    else: 
      if BDC:
        print "I am copying BDC"
        CopyBDC()
      if RD:
        print "I am copying RD"
        CopyRD() 
      if SBS:
        print "I am copying SBS"
        CopySBS()
      if GPL:
        print "I am copying GPL"
        CopyGPL()
      if CFG:
        print "I am copying Config.dll"
        CopyCFG()


  except BuildError, e:
    fail(e.msg)


import fnmatch
import getopt
import os
import shutil
import sys

SolBuild = ''
LPBuild = ''
top = r'c:\ds\trunk'
oldbuild = ''

def CopySolution():
 #copies the local solution7.1 directory to local shares for testing
  Src_dir = 'C:\\Solution7.1'
  test = r'\\builddev.altiris.com\buildtest\DeploymentSolution\ANGELTEST\Solution7.1'
  #builddev = r'\\builddev.altiris.com\buildtest\DeploymentSolution\Latest_TEST\Hampton',
  #scratch = r'\\linus-scratch.altiris.com\Scratch\From_Polaris\DeploymentSolution\Builds\trunk'
  roboOptions = '/Z /R:20 /NP /V'
  os.system("C:\\ds\\trunk\\build\\scripts\\robocopy %s %s %s > robo.log" % (Src_dir, test, roboOptions))

def GetBuildNum(dirname):
    return str('0' + ''.join([x for x in dirname if x.isdigit()]))

def GetSolutionBuild():
  global  SolBuild
  if SolBuild == '':
    GET_BLD = r'\\builddev.altiris.com\buildtest\DeploymentSolution\Daily_Builds\trunk'
    highBuild = max([GetBuildNum(x) for x in os.listdir(GET_BLD)])
    print highBuild
    SolBuild1 = highBuild[3:7]
    SolBuild = int(SolBuild1)
    oldbuild = SolBuild -1
    print oldbuild
    print SolBuild
	
def GetLPBuild():
  global  LPBuild
  if LPBuild == '':
    GET_BLD = r'\\builddev.altiris.com\buildtest\DeploymentSolution\Daily_Builds\trunk\LanguagePacks'
    highestBuild = max([GetBuildNum(x) for x in os.listdir(GET_BLD)])
    print highestBuild
    LPBuild1 = highestBuild[3:7]
    LPBuild = int(LPBuild1)
    print LPBuild
    
def RenameOldSol():
  global SolBuild, oldbuild
  if SolBuild == '':
    GET_BLD = r'\\builddev.altiris.com\buildtest\DeploymentSolution\Daily_Builds\trunk'
    highBuild = max([GetBuildNum(x) for x in os.listdir(GET_BLD)])
    print highBuild
    SolBuild1 = highBuild[3:7]
    SolBuild = int(SolBuild1)
    oldbuild = SolBuild -1
  #src_dir = r'\\builddev.altiris.com\buildtest\DeploymentSolution\DeploymentSolution\Latest_TEST\Hampton\Solution7.1'
  src_dir = 'C:\\Solution7.1'
  dst_dir = 'C:\\Solution7.1.%s.0' % oldbuild
  #dst_dir = r'\\builddev.altiris.com\buildtest\DeploymentSolution\DeploymentSolution\Latest_TEST\Hampton\Solution7.1.%s.0' % oldbuild
  print "renaming existing Solution7.1 directory to Solution7.1.", oldbuild
  if os.path.exists(src_dir):
    os.rename(src_dir, dst_dir)
    
def RenameOldSoltes():
  global oldbuild
  src_dir = 'C:\\Solution7.1'
  dst_dir = 'C:\\Solution7.1.%s.0' % oldbuild
  #src_dir = r'\\builddev.altiris.com\buildtest\DeploymentSolution\DeploymentSolution\Latest_TEST\Hampton\Solution7.1'
  #dst_dir = r'\\builddev.altiris.com\buildtest\DeploymentSolution\DeploymentSolution\Latest_TEST\Hampton\Solution7.1.%s.0' % oldbuild
  print "renaming existing Solution7.1 directory to Solution7.1.", oldbuild
  if os.path.exists(src_dir):
    os.rename(src_dir, dst_dir)

def CallSimpler():
  global top, SolBuild
  if SolBuild == '':
    GET_BLD = r'\\builddev.altiris.com\buildtest\DeploymentSolution\Daily_Builds\trunk'
    highBuild = max([GetBuildNum(x) for x in os.listdir(GET_BLD)])
    print highBuild
    SolBuild1 = highBuild[3:7]
    SolBuild = int(SolBuild1)
  #calls the simpler tool to update the existing good pl.xml Currently good is x64 1017
  print "/prodver ", SolBuild
  cmd = '"%s\\build\\Simpler\\Simpler.exe" /pl "%s\\build\\Simpler\\Altiris Deployment Solution x64.pl.xml" /saveas "C:\\Solution7.1\\Altiris Deployment Solution x64.pl.xml" /product "Altiris Deployment Solution" /prodver 7.1.%s /updatemsi /local "C:\\Solution7.1" /repos "C:\\Solution7.1" /checkprodcodes "*.msi"' % (top, top, SolBuild)
  print cmd
  os.system(cmd)

#This is the main program
if __name__ == '__main__':
    #CallSimpler()
    RenameOldSol()
    #GetSolutionBuild()
    #GetLPBuild()
    #CopySolution()

import os
import subprocess
import string

#Small function to check the availability of network resource. 
def isAvailable(path): 
  winCMD = 'IF EXIST ' + path + ' echo YES' 
  cmdOutPut = subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True).communicate() 
  return string.find(str(cmdOutPut), 'YES',) 

#Small function to check if the mention location is a directory 
def isDirectory(path): 
  winCMD = 'dir ' + path + ' | FIND ".."' 
  cmdOutPut = subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True).communicate() 
  return string.find(str(cmdOutPut), 'DIR',) 

def mapNetworkDrive(drive, networkPath, user, password): 
  #Check for drive availability 
  if isAvailable(drive) > -1: 
    #Drive letter is already in use 
    return -1 

  #Check for network resource availability 
  if isAvailable(networkPath) == -1: 
    print "Path not accessible: ", networkPath 
    #Network path is not reachable 
    return -1 

  #Prepare 'NET USE' commands 
  winCMD1 = 'NET USE ' + drive + ' ' + networkPath 
  winCMD2 = winCMD1 + ' ' + password + ' /User:' + user 
  print "winCMD1 = ", winCMD1 
  print "winCMD2 = ", winCMD2 

  #Execute 'NET USE' command with authentication 
  winCMD = winCMD2 
  cmdOutPut = subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True).communicate() 
  print "Executed: ", winCMD 

  if string.find(str(cmdOutPut), 'successfully',) == -1: 
    print winCMD, " FAILED" 
    winCMD = winCMD1 
  #Execute 'NET USE' command without authentication, incase session already open 
    cmdOutPut = subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True).communicate() 
    print "Executed: ", winCMD 
    if string.find(str(cmdOutPut), 'successfully',) == -1: 
      print winCMD, " FAILED" 
      return -1 
    #Mapped on second try 
    return 1 
  #Mapped with first try 
  return 1 

def unmapNetworkDrive(drive): 
 #Check if the drive is in use 
  if isAvailable(drive) == -1: 
    #Drive is not in use 
    return -1 

 #Prepare 'NET USE' command 
  winCMD = 'net use ' + drive + ' /DELETE' 
  cmdOutPut = subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True).communicate() 
  if string.find(str(cmdOutPut), 'successfully',) == -1: 
    #Could not UN-MAP, this might be a physical drive 
    return -1 
  #UN-MAP successful 
  return 1 

def mapDrive(drive, networkPath, user, password, force=0): 
  print networkPath 
  if (os.path.exists(drive)): 
    print drive, " Drive in use, trying to unmap..." 
    if force: 
      try: 
        win32wnet.WNetCancelConnection2(drive, 1, 1) 
        print drive, "successfully unmapped..." 
      except: 
        print drive, "Unmap failed, This might not be a network drive..." 
        return -1 
    else: 
      print "Non-forcing call. Will not unmap..." 
      return -1 
  else: 
    print drive, " drive is free..." 
  if (os.path.exists(networkPath)): 
    print networkPath, " is found..." 
    print "Trying to map ", networkPath, " on to ", drive, " ....." 
    try: 
      win32wnet.WNetAddConnection2(win32netcon.RESOURCETYPE_DISK, drive, networkPath, None, user, password)
    except: 
       print "Unexpected error..." 
       return -1 
    print "Mapping successful" 
    return 1 
  else: 
    print "Network path unreachable..." 
    return -1   

#This is the main program
if __name__ == '__main__':
  mapNetworkDrive( "m:", "\\\\builddev.altiris.com\\buildtest", "altiris\\build", "build1")
  #unmapNetworkDrive("M:")

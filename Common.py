#commonfuctions used in Gather, Test Build, Official Build usign new gather process

def GetWorkspace():
  global workspace
  #find c:\workspace.txt
  #open and read C:\workspace.txt first line should be the -c workspace name used by that person
  #ie angel-ds is my workspace on SITHLORD-ANGEL
  f = open('c:\\workspace.txt', 'r')
  workspace1 = f.read()
  workspace = workspace1.strip()
  print workspace
  f.close

def GetVersion():
  global version, localtrunk, GatherSBS, want, have
#check to see if --version provided a version if not then we check SBS.want for what we want.
#open the .want file to see what version is wanted options in this file are latest, build number
#ie if we always want latest we would have latest as first line in that file, if we wanted a rdbuild it would be 9266
#if this comes from a DS build it would be build9226
#Source for version for rdeploy
  GET_BLD =  r'\\rdbuild.altiris.com\builds\trunk'
  if version == 'latest':
    print "this is the value for version", version
    f = open (localtrunk + '\\distrib\\scripts\\SBS.have', 'r')
    have = f.read()
    f.close()
    f = open(localtrunk + '\\distrib\\scripts\\SBS.want', 'r')
    want = f.read()
    f.close()
    if want.strip().lower() == 'latest':
      highestbuild = max([int(x) for x in os.listdir(GET_BLD) if x.isdigit()])
      want = highestbuild
    if [int(want)] != [int(have)]:
      print "1 have =", have, "want =", want
      GatherSBS = True
    else:
      print "2 have =", have, "want =", want
      GatherSBS = False
      print "Exiting gather script we have", have, "what we want", want

  else:
    print "I was told to get version", version
    f = open (localtrunk + '\\distrib\\scripts\\SBS.have', 'r')
    have = f.read()
    f.close()
    want = version
    if want != have:
      print "3 have =", have, "want =", want
      GatherSBS = True
    else:
      print "4 have =", have, "want =", want
      GatherSBS = False
      print "Exiting gather script we have", have, "what we want", want

def UpdateHave():
  global want
#checkout and write to have to match the newly gathered version
  os.system("p4 -c %s edit %s" % (workspace, %_HV))
  f = open (localtrunk + '\\distrib\\scripts\\CFG.have', 'w')
  f.write(str(want))
  f.close()

def P4vSync():
  global workspace
  #sync up the workspace with depot
  #os.system("p4 -p %s sync //depot/EMG/NS/Solutions/DS/Trunk/file.ext" % (P4PORT))
  os.system("p4 -c %s sync %s" % (workspace, %_DPT_ZIP))
  os.system("p4 -c %s sync %s" % (workspace, %_DPT_HV))

def P4vCheckout():
  global workspace
 #def CheckOut
 #os.system("p4 -p %s edit //depot/EMG/NS/Solutions/DS/Trunk/file.ext" % (P4PORT))
  os.system("p4 -c %s edit %s" % (workspace, %_DPT_ZIP))

def P4vRevert():
  global workspace
  #os.system("p4 -p %s revert //depot/EMG/NS/Solutions/DS/Trunk/file.ext" % (P4PORT))
  os.system("p4 -c %s revert %s" % (workspace, %_DPT_ZIP))

def P4vSubmit():
  global workspace
  #p4 [g-opts] submit [-r] [-f submitoption] -d description
  #os.system("p4 -p %s submit //depot/EMG/NS/Solutions/DS/Trunk/file.ext" % (P4PORT))
  os.system("p4 -c %s submit -d %d %s " % (workspace, want, %_DPT_ZIP))
  os.system("p4 -c %s submit -d %d %s " % (workspace, want, %_DPT_HV))

def CopyZip():
#this function grabs the new zip file and copies it to local distrib for checkin
    shutil.copy(zipname, DSTRIB_LOCAL)

def ZipIT(fileList, archive): 
    #'fileList' is a list of file names - full path each name 
    #'archive' is the file name for the archive with a full path
    try: 
        a = zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) 
        for f in fileList:
          print "archiving file %s" % (f) 
          a.write(f) 
        a.close() 
        return True 
    except: return False 
  
def dirEntries(dir_name, subdir):
  fileList = []
  #Return a list of file names found in directory 'dir_name' 
  #If 'subdir' is True, recursively access subdirectories under 'dir_name'. 
  #Example usage: fileList = dirEntries(r'H:\TEMP', True) 
  #All files and all the files in subdirectories under H:\TEMP will be added 
  #to the list. 
  for file in os.listdir(dir_name): 
      dirfile = os.path.join(dir_name, file) 
      if os.path.isfile(dirfile): 
         fileList.append(dirfile) 
  # recursively access file names in subdirectories 
      elif os.path.isdir(dirfile) and subdir: 
          print "Accessing directory:", dirfile 
          fileList.extend(dirEntries(dirfile, subdir))

  return fileList

def CleanUP():
#removes the local CFG_DST files from local hard drive
  print "Deleting", zipname
  if os.path.exists(zipname):
    os.remove(zipname)
  print "Deleting", %_DST
  if os.path.exists(%_DST):
    shutil.rmtree(%_DST, ignore_errors=True)
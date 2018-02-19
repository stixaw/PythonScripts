import subprocess
import win32wnet
 
drive_mappings = []
if "Dept XYZ" in myGroups:
    drive_mappings.append(('V:', '\\\\ServerName\\folderName'))
 
for mapping in drive_mappings:
    try:
        # Try to disconnect anything that was previously mapped to that drive letter
        win32wnet.WNetCancelConnection2(mapping[0],1,0)
    except Exception, err:
        print 'Error mapping drive!'
 
    try:
        win32wnet.WNetAddConnection2(DISK, mapping[0], mapping[1])
    except Exception, err:
        if 'already in use' in err[2]:
            # change the drive letter since it's being mis-assigned
            subprocess.call(r'diskpart /s \\%s\path\to\log\change_g.txt' % pdcName)
            # try mapping again
            win32wnet.WNetAddConnection2(DISK, mapping[0], mapping[1])

#win32wnet		
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

def unmapDrive(drive, force=0): 
    #Check if the drive is in use 
    if (os.path.exists(drive)): 
        print "drive in use, trying to unmap..." 
        if force == 0: 
            print "Executing un-forced call..." 
        try: 
            win32wnet.WNetCancelConnection2(drive, 1, force) 
            print drive, "successfully unmapped..." 
            return 1 
        except: 
            print "Unmap failed, try again..." 
            return -1 
    else: 
        print drive, " Drive is already free..." 
        return -1 

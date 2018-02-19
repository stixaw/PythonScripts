import ftplib
import os
import sys
import traceback

print "Files:", sys.argv[1:]

print "Logging in..."
ftp = ftplib.FTP()
ftp.connect(host, port)
print ftp.getwelcome()
try:
    try:
        ftp.login(login, password)
        ftp.cwd(some_directory)
        # move to the desired upload directory
        print "Currently in:", ftp.pwd()

        print "Uploading...",
        fullname = sys.argv[1]
        name = os.path.split(fullname)[1]
        f = open(fullname, "rb")
        ftp.storbinary('STOR ' + name, f)
        f.close()
        print "OK"
        
        print "Files:"
        print ftp.retrlines('LIST')
    finally:
        print "Quitting..."
        ftp.quit()
except:
    traceback.print_exc()
        
raw_input("Press Enter...")


#Connect to FTP

from ftplib import FTP
import os, sys, webbrowser

server = ‘ftp.blah.com’
username = ‘joe’
password = ‘password’

ftp = FTP(server)
ftp.login(username, password)
ftp.retrlines(‘LIST’)
ftp.close()


Angel working commands:
import os
import shutil
import sys
import ftplib
import webbrowser
import traceback

server = 'wiki.epmg.symantec.com'
user = 'cm'
password = 'Iamcm'
wkdir = '//cm//ds//Hampton'
SolBuild = 999
SolDir = 'Solution7.1.%s.0' % (SolBuild)
Src_File = 'C:\\testme.zip'

ftp = ftplib.FTP(server)
ftp.login (user, password)
print ftp.getwelcome()


ftp.cwd(wkdir)
print "Currently in:", ftp.pwd()
if not os.path.exists(SolDir):
  ftp.mkd(SolDir)
ftp.cwd(wkdir + '//' + SolDir)
print "Currently in:", ftp.pwd()

print "Uploading...", Src_File
zip = os.path.split(Src_File)[1]
print zip
ftp.storbinary('STOR ' + zip, open(Src_File, "rb"), 1024)


print ftp.retrlines('LIST')


ftp.quit()
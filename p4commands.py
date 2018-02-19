#test submit function to get it working

import getopt
import os
import shutil
import sys

RD_ZIP = r'//depot/demo_area/rdeploy.zip'
RD_LOC = r'c:\test\Angel\rdeploy.zip'


def P4vsync():
  os.system("p4 -c angel-test sync %s" % (RD_LOC))

def P4vedit():
  os.system("p4 -c angel-test edit %s" % (RD_LOC))

def P4vsubmit():
  os.system("p4 -c angel-test submit -d 'test' %s" % (RD_LOC))

#This is the main program
if __name__ == '__main__':
    
    P4vsync()
    P4vedit()
    P4vsubmit()
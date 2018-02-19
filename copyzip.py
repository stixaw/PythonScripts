import os
import shutil
import sys

StagingPath = 'C:'
BDC_DST = StagingPath + '\\distrib\\bootwiz'
zipname = BDC_DST + '.zip'

localtrunk = 'C:\\ds\\trunk'
DSTRIB_LOCAL = localtrunk + r'\distrib'

if os.path.exists(DSTRIB_LOCAL + zipname):
  os.remove(zipname)
  print "removing zipname"
shutil.copy(zipname, DSTRIB_LOCAL)
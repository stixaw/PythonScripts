
+import os
import sys

Build = '7.1.1252.0'
workspace = 'angel-ds'
top = 'c:\\ds\\trunk'
LPFILES = top + '\\build\\LP-2008\\...'
#submit changes
print "Calling p4 -c %s submit -d '%s' %s " % (workspace, Build, LPFILES)
os.system("p4 -c %s submit -d %s %s " % (workspace, Build, LPFILES))


import os
import sys


psswd = 'ds_build'
P4PORT = 'perforce.ges.symantec.com:1666'
pvalue = os.system("p4 login -p -P %s" % (psswd)) 
print pvalue
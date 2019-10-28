import os
import sys


psswd = 'password'
P4PORT = 'xxxx.com:1666'
pvalue = os.system("p4 login -p -P %s" % (psswd)) 
print pvalue

import os
import shutil
import sys
import subprocess

cmd =  ('c:\\dir.bat')
cmdconsole = 'C:\\windows\\system32\\cmd.exe /C'

subprocess.check_call(cmdconsole + cmd)

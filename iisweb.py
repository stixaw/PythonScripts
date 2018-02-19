import os
import sys

cmd1 = (' cscript "%windir%\\system32\\iisvdir.vbs" /create "Default Web Site" Altiris.DellProvisioning.Web "%WORKSPACE%\\trunk\\DellProvisioning\\Altiris.DellProvisioning.Web"')
cmd2 = (' cscript "%windir%\\system32\\iisvdir.vbs" /create "Default Web Site/Altiris" Dell_Solution "%WORKSPACE%\\trunk\\Solution\\Dell_Solution\\Dell_Solution\DellDeployment.Dell_Solution.Web"')
cmdconsole = 'C:\\windows\\system32\\cmd.exe /C'

os.system(cmdconsole + cmd1)
os.system(cmdconsole + cmd2)
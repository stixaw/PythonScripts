# PYTHON COPY MSI SCRIPT to ali-netapp1.altiris.com

def wnet_connect(server, username = None, password = None):
  global user, pwrd, netpath, host, domain
  networkPath = netpath
  unc = ''.join(['\\\\', host])
  print unc
  try:
   win32wnet.WNetAddConnection2(0, None, unc, None, username, password)
  except Exception, err:
   if isinstance(err, win32wnet.error):
     #Disconnect previous connections if detected, and reconnect.
     if err[0] == 1219:
       win32wnet.WNetCancelConnection2(unc, 0, 0)
       return wnet_connect(host, username, password)
   raise err
# SCript for cleaning up directories and pl.xml on build share

import os
import sys
import time
from datetime import date
from datetime import timedelta
import glob
from optparse import OptionParser
import win32wnet
import shutil

#ugly globals
xDate =''
expDate = ''
releaseName=''


def parseArgs():
	global releaseName, dirPath
	#parses the commandline
	parser = OptionParser("usage: %prog [options] arg1")
	parser.add_option("-n", "--name",
		type="string",
		action="store",
		dest="releaseName",
		default="Orion",
		help="you must supply the release name for the path to the pl directory")
	(options, args) = parser.parse_args()

	print options
	print args
	releaseName = options.releaseName
	print releaseName
	return releaseName

def getDate():
	global xDate, expDate
	#get todays date
	xDate = date.today()
	print 'Today = ', xDate

	#deterimine a week ago
	#offset = (xDate.weekday() - 2) % 7
	expDate =xDate - timedelta(days=14)
	print "Expiration date for comparison = ", expDate
	return expDate, xDate


def compareFiles():
	global xDate, releaseName, expDate
	dirPath = r'\\ali-netapp1.linus.sen.symantec.com\Build\Lindon\%s\ITMS' % (releaseName)
	#get the date from files
	for dirname, dirnames, filenames in os.walk(dirPath):
		for subdirname in dirnames:
			folder = os.path.join(dirname, subdirname)
			folderdate =  date.fromtimestamp(os.path.getctime(folder))
		if expDate > folderdate:
			try:
				print "removing ", folder, "was created ", folderdate, " and is older than ", expDate
				shutil.rmtree(folder)
			except OSError:
				print 'Could not remove', folder
		

def wnet_connect(host, username = None, password = None):
	netpath = r'\\ali-netapp1.linus.sen.symantec.com\Build'
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

if __name__=="__main__":

	wnet_connect('ali-netapp1.linus.sen.symantec.com', username = 'linus' + '\\' + 'ITMSBuild', password = '1TMS8uild')
	parseArgs()
	getDate()
	compareFiles()
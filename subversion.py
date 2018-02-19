import os
import sys
import shutil



def copyPlatformPl():
	pl_tempdst = 'C:\\'
	pl_template = 'platform.pl.xml'
	shutil.copy(pl_tempdst + '\\' + pl_template, './pl/' + pl_template)

def subversionCo(usr,pwd):
	src = 'https://engsrc.engba.symantec.com/svn/SMP/NS/trunk/main/CombinedBuild/PL/CBPPL/'
	dest = './pl'
	#checks out template to be updated
	os.system('svn co '+ src + ' ' + dest + ' --username ' + usr + ' --password ' + pwd)

def subversionCi(usr,pwd):
	pl_template = 'platform.pl.xml'
	Version = '7.1.1059.0'
	os.system('svn ci ./pl/' + pl_template + ' --message "Checking in template from version %s" '% (Version) +  '--username ' + usr + ' --password ' + pwd)

#This is the main program
if __name__ == '__main__':
	copyPlatformPl()
	subversionCi('itmbuild','1TMBui1d')
#Search in pdt files for words or phrases

import os
import sys
import glob
import string
import optparse

findString = ''
pathFile = ''
extFile =''

def getOptions():
	global findString, pathFile, extFile
	"""Setsup and parses the commandline arguments and returns the parse_args result. argv is just sys.argv passed in"""
	parser = optparse.OptionParser("usage: %prog [options] arg1 arg2 arg3")
	parser.add_option('-w', '--word',	
		help='provide the word or string to look for in files you are searching', 
		dest='findString',
		type='string', 
		action='store', 
		default=None)
	parser.add_option('-p', '--path',
		help='provide path to directory of files you are searching',
		dest='pathFile',
		type='string',
		action='store',
		default=None)
	parser.add_option('-e', '--ext',
		help='provide the extension of the files you want to search',
		dest='extFile',
		type='string',
		action='store',
		default=None)
	(options, args) = parser.parse_args()
	
	if len(args) != 3:
		parser.error("incorrect number of arguments")

	print options
	findString = options.findString
	extFile = options.extFile
	pathFile = options.pathFile

def searchFiles():
	global findString, pathFile, extFile

	searchDir =(pathFile + '\\*.' + extFile)
	print searchDir
	file_list=[]
	search_results=[]

	for filename in glob.glob(searchDir):
		file_list.append(filename)
		print filename
		with open(filename) as f:
			for line in f:
				if findString in line:
					search_results.append(filename + ',' + line)
					print filename + ',' + line
					textfile = open('C:\\SearchResults.txt', 'w')
					textfile.writelines((line + '\n' for line in search_results))
					textfile.close
		f.close()



if __name__ == '__main__':
	getOptions()
	searchFiles()
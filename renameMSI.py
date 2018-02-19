import os

PCA_list = ["ProductSolution_x64.msi",
	"PraticeSolution_x86.msi",
	]
DS_list = ["DSSolution_x64.msi",
	"TESTSolution_x86.msi",
	]
Doc_list = ["Altiris_DSDocumentation_x64.msi",
	"Symantec_PCADocumentation_x64.msi",
	]

def releaseSolName(brand,version,list):
	global Src_Dir				
	for msi in list:
		if os.path.exists(Src_Dir + "\\" + msi):
			name,arch = os.path.splitext(msi)[0].split('_')    
			newname = "%s_%s_%s_%s.msi" %(brand, name, version, arch)
			print "renaming ", msi, "to ", newname
			os.rename(Src_Dir + "\\" + msi, Src_Dir + "\\" + newname)
		else:
			print "Rename function failed", msi, "does not exist"
			sys.exit(3)
			
def releaseDocName(version,list):
	global Src_Dir
	for msi in list:
		if os.path.exists(Src_Dir + "\\" + msi):
			brand,name,arch = os.path.splitext(msi)[0].split('_')    
			newname = "%s_%s_%s_%s.msi" %(brand, name, version, arch)
			print "renaming ", msi, "to ", newname
			os.rename(Src_Dir + "\\" + msi, Src_Dir + "\\" + newname)
		else:
			print "Rename function failed", msi, "does not exist"
			sys.exit(3)


#Main
if __name__ == '__main__':
	releaseSolName('Altiris','7_1_sp2',DS_list)
	releaseSolName('Symantec', '7_1_sp2',PCA_list)
	releaseDocName('7_1_sp2',Doc_list)
	
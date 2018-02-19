#pickling program
#data storage and maniuplation

import cPickle
import shelve

print "\nPickling lists"
variety = ["sweet", "dill", "koscher"]
shape = ["whole", "spear", "chip"]
brand = ["Vlassic", "Heinz", "Claussen"]
pickle_file=open("pickle1.dat", "w")
cPickle.dump(variety, pickle_file)
cPickle.dump(shape, pickle_file)
cPickle.dump(brand, pickle_file)
pickle_file.close()

pickle_file=open("pickle1.dat", "r")
variety = cPickle.load(pickle_file)
shape = cPickle.load(pickle_file)
brand = cPickle.load(pickle_file)
print variety, "\n", shape,  "\n", brand
pickle_file.close

print "\nShelving lists"
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet", "dill", "koscher"]
pickles["shape"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Vlassic", "Heinz", "Claussen"]
pickles.sync()

print "\nRetrieving shelved data"
for key in pickles.keys():
	print key, "-", pickles[key]
pickles.close()



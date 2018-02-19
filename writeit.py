#Write it program
#write to text

import os
import sys
import datetime
import time

print "\nCreating a txt file to write"
text_file=open("C:\\write_it.txt", "w")
text_file.close()

print "\nwriting to the txt file"
TIM_STMP = time.strftime("%Y%m%d%H%M", time.gmtime())
print TIM_STMP
text_file=open("C:\\write_it.txt", "w")
text_file.write("line 1, %s \n" % (TIM_STMP))
text_file.write("line 2, %s \n" % (TIM_STMP))
text_file.write("line 3, %s \n" % (TIM_STMP))
text_file.close()
text_file=open("C:\\write_it.txt", "r")
print text_file.read()
text_file.close()


print "\nCreating a txt file to write"
text_file=open("C:\\write_it.txt", "w")
text_file.close()

print "\nwriting to the txt file"
lines= ["line 1\n", "line 2\n", "line 3\n"]
text_file=open("C:\\write_it.txt", "w")
text_file.writelines(lines)
text_file.close()
text_file=open("C:\\write_it.txt", "r")
print text_file.read()
text_file.close()
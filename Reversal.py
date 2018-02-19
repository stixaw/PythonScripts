#Reversal
#
#takes a string provided by the user and prints it backwards 


#get the string from the user
message = raw_input("\nWhat is your message: ")

#message = message[::-1]


message =list(message)
message.reverse()
message =''.join(message)

print message

raw_input("\nPress enter to exit")


"""function
def reverse(chars):
aa = array.array('c', chars)
aa.reverse()
return aa.tostring() 
"""

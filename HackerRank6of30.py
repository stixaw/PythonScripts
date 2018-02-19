Python answers:

for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])

for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])
	
'''The colon, inside an array index, can set up to 3 numbers/parameters:
The first one is the "from" number (included), the second is the "to" number (excluded), and the third is the "pace". 
a[::2] will retrieve all array items (since it does not set up any from or to, and set the "pace"), starting from index 0, incrementing the index two by two and accessing all even indexes (0,2,4,6, and so on).
s[1::2] will retrieve all array items, from index 1, incrementing the index two by two and accessing all odd indexes (1,3,5,7,9, and so on).

This is Python's syntax for slicing lists: alist[start:end:step]. You can hide these values to take their default, for example: alist[::] means a full copy of the list. alist[1:3] slices a list taking item from index 1 to index 3 (non-inclusive).
alist[::2] makes makes a new list taking every other item from alist starting at 0.'''

def inputs():
    global S
    S = input() 
    if (len(S) in range (2, 10001)):
        s1 = S[0::2]
        s2 = S[1::2]
        print (s1 + " " +s2)    

T = int(input())
if (T>=1 and T<=10):
    for i in range (0,T):
        inputs()
		

for i in range(int(input().strip())):
    print((lambda x: x[::2] + ' ' + x[1::2])(input().strip())) 
	
	
for i in range(int(raw_input())):
	s=raw_input()
	print(s[::2]+" "+s[1::2]) 
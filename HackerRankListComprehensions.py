'''
Can you tell me how python carries out list comprehension internally? 
How come this generates lists in lexicographic increasing order (i.e z increases first, 
then y, then x)?
It is in lexographical order due to the nature of the loops. Spaced out it looks somewhat like

for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if a + b + c != n:
                print(stuff is here)
We start at [0,0,0]. Then c will increment to get to [0,0,1] When c hits [0,0,z], we get [0,1,0] as the next in the loop. 
This pattern continues and gives us the lexographical ordering required of the output'''


if __name__ == '__main__':
	x = int(input())
	y = int(input())
	z = int(input())
	n = int(input())

	print([[a, b, c] for a in range(0,x+1) for b in range(0, y+1) for c in range (0,z+1) if a + b + c != n])


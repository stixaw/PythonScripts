HankerRank day 5 of 30:
Task 
Given an integer, , print its first multiples. Each multiple (where ) 
should be printed on a new line in the form: n x i = result.

Input Format
A single integer, 

Solution python 2:
import sys


n = int(raw_input().strip())

for x in range(1, 11):
    result = n * x
    print("%s x %s = %s" % (n, x, result))

	

Python 3:
    for i in range(1,11):
        print (N, "x", i, "=", (N*i))
		

In Java:
for (int i = 1; i <= 10; i++) {
  System.out.println(n+""+" x "+i+" = "+(n*i));
  
C#:
    for(int i=1;i<=10;i++)
    {
        Console.WriteLine("{0} x {1} = {2}",n,i,n*i);
    }
}
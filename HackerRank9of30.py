import sys

def factorial1(n):
	# Complete this function
	if (n == 1):
		result = 1
	else:
		result = (n * factorial(n - 1))
	return(result)
	
def factorial(n):
	r = 1
	for _ in range(1,n+1):
		r *= _
	return r

#Lambda version:
#factorial = lambda x : 1 if x<=1 else x*factorial(x-1)
#print(factorial(int(input())))

#java
'''import java.util.*;

public class Solution 
{

    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        System.out.println( factorial(scan.nextInt()) );
    }
        
    public static long factorial( int n )
    {
        return (n == 1) ? 1 : n*factorial(n-1) ;
    }
}'''

#java:
''' static int factorial(int n){
	return n >= 1 ? n * factorial(n-1) : 1;
}'''
#python:
'''def Factorial(num):
    if num == 1:
        return 1
    else:
        return (num * Factorial(num-1))'''


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
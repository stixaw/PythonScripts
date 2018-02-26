'''Read an integer N . For all non-negative integers i < N , print i**2 .'''

if __name__ == '__main__':
    n = int(input())
    
    for x in range(n):
        if (x < n)& (x >= 0):
            result = x**2
            print(result)
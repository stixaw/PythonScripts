import sys

def factorial(n):
    # Complete this function
    count = n
    result = 0
    while n >0:
        result = n * (n-1)
        count = count - 1
    return(result)
        


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
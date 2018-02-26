''' Read integer N without using string functions print 123...
Note that "..." represents the values in between.'''

if __name__ == '__main__':
    n = int(input())
    
    for x in range(1, n + 1):
        print(x, end='')
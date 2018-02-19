def plusMinus(arr):
    posNum = 0
    negNum = 0
    zeros = 0
    myList = list(arr)
    s1 = len(myList)
    
    for i in range(s1):
        if arr[i] == 0:
            zeros += 1
        elif arr[i] > 0:
            posNum += 1
        elif arr[i] < 0:
            negNum += 1
    print(format(posNum/float(s1),".6f"))
    print(format(negNum/float(s1),".6f"))
    print(format(zeros/float(s1),".6f"))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
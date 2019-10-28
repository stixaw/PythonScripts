import sys

a = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    a.append(arr_temp)

max_sum = -63

for i in range(4):
    for j in range(4):
        check_sum = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][
            j + 2]

        if check_sum > max_sum:
            max_sum = check_sum

print max_sum

# option 2:
print(max([sum(arr[i-1][j-1:j+2] + [arr[i][j]] + arr[i+1][j-1:j+2]) for j in range(1, 5) for i in range(1, 5)]))

# another option:
def hourglassSum(arr):
    li=[]
    for i in range(len(arr)-2):

        for j in range(len(arr)-2):

          li.append(sum(arr[i][j:j+3]+arr[i+2][j:j+3])+arr[i+1][j+1])

    return max(li)
import sys
import os

def hourGlassSum(arr):
    results = []
    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            results.append(s)
    print(max(results))

if __name__ == "__main__":
	arr = []
	for arr_i in range(6):
		arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
		arr.append(arr_t)

	hourGlassSum(arr)
import os
import sys


dict_test = {'thing': 'monkey', 'type': 'mammal', 'likes': {'foods': ['bananas', 'nuts']}}

for k in dict_test:
    print(dict_test[k])

print(dict_test['likes'])

print(dict_test['likes'][['foods'][0]])



print(dict_test['likes'][['foods'][0]][1])
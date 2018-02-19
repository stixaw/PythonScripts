#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

foo = arr[::-1]
foostring = ""
for i in foo:
    if len(foostring) == 0:
        foostring += str(i)
    else:
        foostring += " " + str(i)
print(foostring)


Python one liner:
print(" ".join(map(str, arr[::-1])))
'''Let's start from the Inside of map function, the arr[::-1] will reverse the List from [1, 2, 3, 4] to [4, 3, 2, 1] . Now map takes a Function and a sequence. So you have to convert your List to string data type to perform join operation. So after that you would be having ['4', '3', '2', '1'] as a str Now you have to Join each other with a space in between, hence you use " ".join(blahblah) .Therefore, you get output. '''

Python 3:
print(' '.join(str(x) for x in arr[::-1]))

Javascript:
console.log(arr.reverse().toString().replace(/,/g,' '));

console.log(arr.reverse().join(' '));

java
public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];
        for(int i=0; i < n; i++){
            arr[i] = in.nextInt();
        }
        
        for(int i=n-1; i>=0; i--){
            System.out.print(arr[i]+" ");
        }
        in.close();
    }

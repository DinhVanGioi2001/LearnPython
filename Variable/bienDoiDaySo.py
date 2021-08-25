import math

string = input()
arr = string.split()
for i in range(0, 4):
    arr[i] = int(arr[i])
for i in range(0, 4):
    if i == 3:
        arr[i] = abs(arr[i] - arr[0])
    else:
        arr[i] = abs(arr[i] - arr[i+1])
for i in range(0, 3):
    if(arr[i] != arr[i+1]):
        count += 1

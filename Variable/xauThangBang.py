import math
p = "abcdefghijklmnopqrstuvwxyz"
test = int(input())
while test:
    test -= 1
    str = input()
    check = 1
    mid = int(len(str)/2)
    strReverse = str[::-1] #start:stop:step
    for i in range(0, mid + 1):
        if abs(p.find(str[i]) - p.find(str[i+1])) != abs(p.find(strReverse[i]) - p.find(strReverse[i+1])):
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO")
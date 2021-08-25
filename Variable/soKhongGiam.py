test = int(input())
while test > 0:
    test -= 1
    n = input()
    check = 0
    j = n[0]
    for i in n:
        if(i < j):
            check = 1
            break
        j = i
    if check == 0:
        print("YES")
    else:
        print("NO")

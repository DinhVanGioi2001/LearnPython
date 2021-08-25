test = int(input())
while(test > 0):
    test -= 1
    line = input()
    sum = 0
    k = int(line[0])
    check = 1
    for i in range(len(line)):
        j = int(line[i])
        sum += j
        if i > 0:
            h = j - k
            if h != 2 and h != -2:
                check = 0
                break
        k = j
    if sum % 10 == 0 and check == 1:
        print("YES")
    else:
        print("NO")
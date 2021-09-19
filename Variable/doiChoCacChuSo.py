test = int(input())
while test > 0:
    test -= 1
    n = input()
    res = [int(i) for i in n]
    tmp, check = len(res), 0
    for i in range(0, len(res)):
        if res[tmp - i-1] < res[tmp-i-2]:
            a = res[tmp-i-1]
            res[tmp-i-1] = res[tmp-i-2]
            res[tmp-i-2] = a
            check =1
            break
    if res[0] == 0 or check == 0:
        print("-1")
    else:
        for i in res:
            print(i, end="")
        print()
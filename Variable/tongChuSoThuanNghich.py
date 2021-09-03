test = int(input())
while test > 0:
    test -= 1
    sum = 0
    n = input()
    for i in n:
        sum += int(i)
    res = 0
    tmp = sum
    while tmp > 0:
        res = res*10 + tmp % 10
        tmp = int(tmp/10)
    if res == sum and sum > 9:
        print("YES")
    else:
        print("NO")
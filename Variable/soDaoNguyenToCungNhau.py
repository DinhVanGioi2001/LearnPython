def lcm(n, m):
    while n*m != 0:
        if n > m:
            n %= m
        else:
            m %= n
    return n+m == 1

test = int(input())
while test > 0:
    test -= 1
    n = input()
    sum1 = 0; sum2 = 0
    tmp = 1
    for i in n:
        sum1 = sum1 * 10 + int(i)
        sum2 = int(i) * tmp + sum2
        tmp *= 10
    if lcm(sum1, sum2) == 1:
        print("YES")
    else:
        print("NO")
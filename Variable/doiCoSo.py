list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
test = int(input())
while test > 0:
    test -= 1
    tmp = input().split()
    n, base = int(tmp[0]), int(tmp[1])
    res = []
    while n > 0:
        res.append(n % base)
        n //= base
    res.reverse()
    for i in res:
        print(list[int(i)], end="")
    print()
import math
def lcm(n, m):
    while n*m != 0:
        if n > m:
            n %= m
        else:
            m %= n
    return n+m == 1
str = input()
str = str.split()
n = int(str[0])
k = int(str[1])
tmp1 = math.pow(10, k -1)
tmp2 = math.pow(10, k)
count = 0
for i in range(int(tmp1), int(tmp2)):
    if count == 10:
        count = 0
        print()
    if lcm(n, i) == 1:
        count += 1
        print(i, end=' ')
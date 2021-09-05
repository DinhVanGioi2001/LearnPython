import math
def lcm(n, m):
    while n*m != 0:
        if n > m:
            n %= m
        else:
            m %= n
    return n+m == 1

str = input().split()
l = int(str[0])
r = int(str[1])
for i in range(l, r - 2):
    for j in range(l+1, r-1):
        if lcm(i, j):
            for k in range(l + 2, r):
                if lcm(j, k) == 1 and lcm(i, k) == 1:
                    print("(", i, ", ", j, ", ", k, ")", sep="")
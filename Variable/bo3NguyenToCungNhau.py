import math
def lcm(n, m):
    while m > 0:
        t = n % m
        n = m
        m = t
    return n

str = input().split()
l = int(str[0])
r = int(str[1])
for i in range(l, r - 2):
    for j in range(l+1, r-1):
        for k in range(l + 2, r):
            if lcm(i, j) == 1 and lcm(j, k) == 1 and lcm(i, k) == 1:
                print("(", i, ", ", j, ", ", k, ")", sep="")
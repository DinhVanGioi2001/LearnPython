import math
def isPrime(n):
    if n < 2: return 0
    tmp = math.sqrt(n) + 1
    for i in range(2, int(tmp)):
        if n % i == 0:
            return 0
    return 1

test = int(input())
while test > 0:
    test -= 1
    n = input()
    sum = 0
    l = len(n)
    for i in range(l-4, l):
        sum = sum * 10 + int(n[i])
    if isPrime(sum):
        print("YES")
    else:
        print("NO")
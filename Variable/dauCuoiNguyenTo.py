import math
def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, n):
        if(n % i == 0):
            return 0
    return 1

test = int(input())
while test > 0:
    test -= 1
    n = input()
    l = len(n)
    sum1 = 0; sum2 = 0
    for i in range(0, 3):
        sum1 = sum1 * 10 + int(n[i])
    if isPrime(sum1):
        for i in range(l - 3, l):
            sum2 = sum2 * 10 + int(n[i])
        if isPrime(sum2):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
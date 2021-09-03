import math

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, n):
        if (n % i == 0):
            return 0
    return 1

test = int(input())
while test > 0:
    test -= 1
    n = input()
    nt = 0; knt = 0
    if isPrime(len(n)):
        for i in range(len(n)):
            if isPrime(int(n[i])):
                nt += 1
            else:
                knt += 1
        if nt > knt:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
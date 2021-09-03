import math

test = int(input())

def isPrime(n):
    if n < 2: return 0
    tmp = math.sqrt(n) + 1
    for i in range(2, int(tmp)):
        if n % i == 0:
            return 0
    return 1

while test > 0:
    test -= 1
    sum = 0
    n = input()
    for i in n:
        sum += int(i)
    if isPrime(sum) == 1:
        print("YES")
    else:
        print("NO")
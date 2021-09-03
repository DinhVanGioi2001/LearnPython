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
    check = 1
    n = input()
    for i in range(0, len(n)):
        tmp = isPrime(int(n[i]))
        if isPrime(i) == 1:
            if tmp == 0:
                check = 0
                break
        else:
            if tmp == 1:
                check = 0
                break
    if check == 1:
        print("YES")
    else:
        print("NO")
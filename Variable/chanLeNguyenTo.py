import math
def isPrime(n):
    if n < 2: return 0
    tmp = math.sqrt(n)
    for i in range(2, int(tmp)):
        if n % i == 0:
            return 0
    return 1

test = int(input())
while test > 0:
    test -= 1
    n = input()
    sum = 0
    check = 1
    for i in range(0, len(n)):
        if i % 2 == 0:
            if int(n[i]) % 2 == 0:
                sum += int(n[i])
            else:
                check = 0
                break
        else:
            if int(n[i]) % 2 == 1:
                sum += int(n[i])
            else:
                check = 0
                break
    if check == 1 and isPrime(sum) == 1:
        print("YES")
    else:
        print("NO")
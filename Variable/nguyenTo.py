import math
test = int(input())
def gcd(a, b):
    while b:
        a, b = b, a % b # kiem tra toi khi a = 1 b = 0
    return a            # Vd 2 3 => 3 2 => 2 1 => 1 0 => return

def ntCungNhau(a, b):
    return gcd(a, b) == 1

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return 0
    return 1
while test:
    test -= 1
    n = int(input())
    count = 0
    for i in range(1, n):
        if(ntCungNhau(i, n)):
            count += 1
    if isPrime(count):
        print("YES")
    else:
        print("NO")
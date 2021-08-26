def isPrime(n):
    if n < 2: return 0
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return 0
    return 1

n = int(input())
str = input()
arr = str.split()
for i in range(0, len(arr)):
    arr[i] = int(arr[i])
hashNT = dict()
for i in arr:
    if i in hashNT:
        hashNT[i] += 1
    else:
        hashNT[i] = 1
for i in hashNT:
    if(isPrime(i)):
        print(i, hashNT[i])
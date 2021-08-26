def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return 0
    return 1

str = input()
arr = str.split()
n1 = int(arr[0])
n2 = int(arr[1])
listPrime = []
i = n1 + 1
n = 2
while i:
    if isPrime(n):
        listPrime.append(n)
        i -= 1
        n += 1
    else:
        n += 1
sum = n2
print(n2, " ", end="")
for i in range(0, n1):
    sum = listPrime[i] + sum
    print(sum, " ",end='')
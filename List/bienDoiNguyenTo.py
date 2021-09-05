def SieveOfEratosthenes(n): #sang nguyen to
    prime = [True for i in range(2 * n + 1)]
    p = 2
    while ( p * p <= 2 * n ): #tim trong khoang căn của 2 * n
        if prime[p] == True:
            i = p * p
            while i <= n * 2:
                prime[i] = False
                i += p
        p += 1
    primes = []
    for p in range(2, (2 * n) + 1):
        if prime[p]:
            primes.append(p)
    return primes
def minChanges(arr):
    n = len(arr)
    ans = 0
    maxi = max(arr) #tim phan tu max cua mang
    primes = SieveOfEratosthenes(maxi) # goi dem ham sang nguyen to
    for i in range(n):
        x = -1
        for j in range(len(primes)): # tim phan tu nto dau tien lon hon arr[i]
            if arr[i] == primes[j]:
                x = j
                break
            elif arr[i] < primes[j]:
                x = j # lay thu tu cua so nguyen to
                break
        minm = abs(primes[x] - arr[i])

        if (x > 1):
            minm = min(minm, abs(primes[x - 1] - arr[i]))
        ans = max(ans, minm)
    return ans

n = int(input())
str = input().split()
arr = []
for i in str:
    arr.append(int(i))
print(minChanges(arr))
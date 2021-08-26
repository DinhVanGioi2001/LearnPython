def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b
def prime(a, b):
    return gcd(a, b) == 1

n = int(input())
str = input()
arr = str.split()
for i in range(0, n):
    arr[i] = int(arr[i])
arr.sort()
for i in range(0, n - 1):
    for j in range(i+1, len(arr)):
        if(prime(arr[i], arr[j])):
            print(arr[i], arr[j])
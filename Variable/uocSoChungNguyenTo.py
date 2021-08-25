import math

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, n):
        if(n % i == 0):
            return 0
    return 1
test = int(input())
while(test):
    test -= 1
    line = input()
    list = line.split(" ")
    number1 = int(list[0])
    num2 = int(list[1])
    tmp = math.gcd(number1, num2)
    x = str(tmp)
    sum = 0
    for i in x:
        sum += int(i)

    if(isPrime(sum)):
        print("YES")
    else:
        print("NO")
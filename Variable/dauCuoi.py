test = int(input())
while(test > 0):
    test -= 1
    n = input()
    sum1 = 0; sum2 = 0
    for i in range(0, 2):
        k = int(n[i])
        sum1 = sum1 * 10 + k
    length = len(n)
    for i in range(length - 2, length):
        k = int(n[i])
        sum2 = sum2 * 10 + k
    if(sum1 == sum2):
        print("YES")
    else:
        print("NO")
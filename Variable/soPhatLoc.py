test = int(input())
while(test > 0):
    test -= 1
    n = input()
    sum = 0
    length = len(n)
    for index in range(length-2, length):
        k = int(n[index])
        sum = sum*10 + k
    if(sum == 86):
        print("YES")
    else:
        print("NO")
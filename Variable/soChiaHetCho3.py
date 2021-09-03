test = int(input())
while test > 0:
    test -= 1
    sum = 0
    n = input()
    for i in n:
        sum += int(i)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")
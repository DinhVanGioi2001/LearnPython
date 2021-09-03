test = int(input())
while test > 0:
    test -= 1
    n = input()
    sum = 0
    mul = 1
    check = 1
    for i in range(len(n)):
        if i % 2 == 0:
            sum += int(n[i])
        elif i % 2 == 1 and int(n[i]) != 0:
            check = 0
            mul *= int(n[i])
    if check == 1:
        mul = 0
    print(sum, mul, sep=" ")
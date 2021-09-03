test = int(input())
while test > 0:
    test -= 1
    mul = 1
    n = input()
    for i in n:
        if int(i) == 0:
            pass
        else:
            mul *= int(i)
    print(mul)
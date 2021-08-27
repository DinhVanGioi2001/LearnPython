test = int(input())
while test:
    test -= 1
    str = input()
    sum = 0
    res = []
    for i in range(0, len(str)):
        if str[i].isnumeric():
            sum += int(str[i])
        else:
            res.append(str[i])
    res.sort()
    for i in range(0, len(res)):
        print(res[i], end='')
    print(sum)
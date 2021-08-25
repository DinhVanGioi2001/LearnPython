test = int(input())
while(test > 0):
    test -= 1
    str = input()
    j = str[0]
    dem = 0
    for i in str:
        if(i == j):
            dem += 1
        else:
            print(dem, end='')
            print(j, end='')
            j = i
            dem = 1
    print(dem, end='')
    print(j)
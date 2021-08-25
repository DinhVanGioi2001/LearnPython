test = int(input())
while(test > 0):
    test -= 1
    str = input()
    j = str[0]
    for i in str:
        if(i.isnumeric()):
            length = int(i)
            for k in range(length):
                print(j, end='')
        else:
            j = i
    print("\n")
test = int(input())
while test:
    test -= 1
    f1 = 1; f2 = 1; fn = 0
    str = input()
    arr = str.split()
    begin = int(arr[0])
    end = int(arr[1])
    listFibo = [0, 1, 1]
    for i in range(1, end):
        fn = f1 + f2
        listFibo.append(fn)
        f1 = f2
        f2 = fn
    for i in range(begin, end+1):
        print(listFibo[i], " ", end='')
    print("")
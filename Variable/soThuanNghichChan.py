test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    for i in range(22, n, 22): #buoc nhay 22 vi 22-44-66-88-2002-2222...
        check = 1
        count = 0
        sum = 0
        m = i;
        while m > 0:
            tmp = m % 10
            count += 1
            if tmp % 2 != 0:
                check = 0
                break
            sum = sum * 10 + tmp
            m //= 10
        if check == 1 and count % 2 == 0:
            if sum == i:
                print(i, end=" ")
    print()
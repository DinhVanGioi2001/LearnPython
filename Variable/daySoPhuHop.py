test = int(input())
while test:
    test -= 1
    check = 1
    n = int(input())
    str1 = input(); str2 = input()
    arr1 = str1.split(); arr2 = str2.split()
    arr1.sort()
    arr2.sort()
    print(arr1)
    for i in range(0, n):
        if arr1[i] > arr2[i]:
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO")
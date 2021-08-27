test = int(input())
while test:
    test -= 1
    check = 1
    n = int(input())
    str1 = input(); str2 = input()
    arr1 = str1.split()
    arr2 = str2.split()
    for i in range(0, n):
        arr1[i] = int(arr1[i])
        arr2[i] = int(arr2[i])
    arr1.sort()
    arr2.sort()
    for i in range(0, n):
        if arr1[i] > arr2[i]:
            print("NO")
            check = 0
            break
    if check == 1:
        print("YES")
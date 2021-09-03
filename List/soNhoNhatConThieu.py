n = int(input())
arr = input().split()
for i in range(0, n):
    arr[i] = int(arr[i])
check = 1
arr.sort() # can sap xep lai vi co the mang chua theo thu tu
for i in range(0, n-1):
    if arr[i+1] - arr[i] > 1: # kiem tra neu 2 ptu chenh nhau hay khong
        print(arr[i] + 1) # in ra a[i] + 1 la ptu nho nhat
        check = 0
        break

if check:
    print(arr[n-1] + 1)
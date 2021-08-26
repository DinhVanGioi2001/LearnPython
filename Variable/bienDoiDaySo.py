import math
str = input()

test, count = 0, 0
arr = str.split()
tmp = len(arr)
p = []
for i in range(0, tmp):
    arr[i] = int(arr[i])
# su dung ham set khong chua phan tu trung lap de xem cac phan tu da trung nhau chua
for i in set(arr): # kiem tra xem co thuoc truong hop dac biet khong
    test = i       # chang han 1 1 1 1
while test != 0:
    count = 0
    while len(set(arr)) > 1: # kiem tra neu khac truong hop nhu 1 1 1 1 || 0 0 0 0
        count += 1
        for i in range(0, tmp):
            if i == tmp-1:
                p.append(abs(arr[i] - arr[0]))
            else:
                p.append(abs(arr[i] - arr[i+1]))
        for i in range(0, tmp):
            arr[i] = p.pop()
    # in ra count la so lan de mang bang nhau
    print(count)
    # nhap lai mang va kiem tra xem co phai 0 0 0 0 hay khong
    str = input()
    arr = str.split()
    tmp = len(arr)
    for i in range(0, tmp):
        arr[i] = int(arr[i])
    for i in set(arr):
        test = i
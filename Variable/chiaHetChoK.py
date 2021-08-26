line = input()
arr = line.split()
for i in range(0, len(arr)):
    arr[i] = int(arr[i])
tmp = arr[1]
count = 1
result = []
'''VD: 10 6 40 
6*2 % 10 = 2    6*3 % 10 = 8...
2, 8,... la nhung ket qua can in ra man hinh'''
while tmp <= arr[2]:
    # count += 1  Khong de tren dau: Vd 3 6 40 thi ket qua la 9 15... Thieu 3 o tren dau
    tmp = arr[1] * count
    if tmp > arr[2]:
        break
    if tmp - arr[0] > 0:
        result.append(tmp - arr[0])
    count += 1 #th 3 6 40 ket qua se la 3 9 15... => du th de xet
if len(result) == 0: #neu khong co gia tri nao duoc bo sung vao result
    print("-1")
else:
    for i in result:
        print(i," ", end='')
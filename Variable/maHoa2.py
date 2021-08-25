p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

n = input()
arr = n.split()
k = int(arr[0])
line = arr[1]
res = []

while k:
    res.clear()
    for i in line:
        res.append(p[(p.find(i) + k) % 28]) #them vao phan tu thu (i+k)%28
    res.reverse()
    for i in res:
        print(i, end='')
    print("")

    i = input()
    if(i == '0'):
        break
    else:
        arr = i.split()
        k = int(arr[0])
        line = arr[1]
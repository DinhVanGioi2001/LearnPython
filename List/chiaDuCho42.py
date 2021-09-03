tmp = 0
arr = []
while tmp < 10:
    str = input()
    str = str.split()
    for i in str:
        tmp += 1
        arr.append(int(i))
res = []
count = 0
for i in arr:
    a = i % 42;
    check = 1
    for i in res:
        if a == int(i):
            check = 0
            break
    if check == 1:
        res.append(a)
        count += 1
print(count)
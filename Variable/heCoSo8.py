n = input()

while(len(n) % 3 != 0):
    n = '0' + n
a = list(n)
a.reverse()
tmp = 1
sum = 0
res = []
for i in range(0, len(a)):
    if tmp == 3:
        sum += int(a[i])*4
        res.append(sum)
        tmp = 1
        sum = 0
    else:
        sum += int(a[i])*tmp
        tmp += 1
res.reverse()
for i in range(0, len(res)):
    print(res[i], end='')
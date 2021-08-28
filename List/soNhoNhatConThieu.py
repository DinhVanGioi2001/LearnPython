n = int(input())
s = input()
a = s.split()
for i in range(0, n):
    a[i] = int(a[i])
minNum = a[0] + 1
check = 1
for i in range(1, n):
    if minNum == a[i]:
        minNum += 1
    else:
        print(minNum)
        check = 0
        break
if check == 1:
    print(a[-1] + 1)
# wa
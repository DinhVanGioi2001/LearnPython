n = int(input())
line = input()
list = line.split(" ")
for i in range(0, n):
    list[i] = int(list[i])
count = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        if list[i] > list[j]:
           count += 1
print(count)
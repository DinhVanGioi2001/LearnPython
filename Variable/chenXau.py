str1 = input()
str2 = input()
n = int(input())
str1 = list(str1)
str1.insert(n-1, str2)
for i in str1:
    print(i, end='')
str = input()

hoa = 0; thuong = 0
for i in str:
    j = i
    if(i == j.upper()):
        hoa += 1
    else:
        thuong += 1
if hoa > thuong:
    print(str.upper())
else:
    print(str.lower())
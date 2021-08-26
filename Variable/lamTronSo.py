test = int(input())

while test:
    test -= 1
    s = input()
    s = list(s) #Vd so: 12345
    s.reverse() #dao nguoc chuoi => 54321
    for i in range(0, len(s) - 1):
        if int(s[i]) >= 5: # kiem tra xem co the lam tron len hay khong
            s[i+1] = int(s[i+1]) + 1 # chuoi tren tro thanh 55321
    print(s[-1], end='') #in ra ki tu cuoi cung la ki tu 1
    for i in range(0, len(s) - 1): #in them so 0 dang sau
        print("0", end='')
    print("")
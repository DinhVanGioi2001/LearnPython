test = int(input())
while test > 0:
    test -= 1
    n = input()
    count = 0
    check = 1
    if int(n[2]) == int(n[1]):
        print("NO")
    else:
        for i in range(0, len(n) - 2):
            if i % 2 == 0:
                count += 1
                if int(n[i]) != int(n[i+2]):
                    check = 0
                    break
            else:
                count += 1
        if check == 1 and count % 2 == 1:
            print("YES")
        else:
            print("NO")
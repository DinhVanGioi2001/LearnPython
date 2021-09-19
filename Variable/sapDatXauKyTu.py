test = int(input())
c = 0
while test > 0:
    test -= 1
    c += 1
    str1 = input()
    line1 = [i for i in str1]
    str2 = input()
    line2 = [i for i in str2]
    line1.sort()
    line2.sort()
    check = 1
    if len(line1) == len(line2):
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                print("Test ", c , ": ",sep="", end='')
                print("NO")
                check = 0
                break
        if check == 1:
            print("Test ", c , ": ",sep="", end='')
            print("YES")
    else:
        print("Test ", c , ": ",sep="", end='')
        print("NO")
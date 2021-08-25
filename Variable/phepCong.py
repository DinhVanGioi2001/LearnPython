line = input()

sum = 0; c = 0
for i in line:
    if(i.isnumeric() and c < 2):
        sum += int(i)
        c += 1
    elif(i.isnumeric() and c >= 2):
        if(sum == int(i)):
            print("YES")
        else:
            print("NO")
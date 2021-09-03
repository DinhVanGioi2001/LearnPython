n = input()

def sum(n):
    tmp = 0
    for i in n:
        if i == '-':
            tmp += ord('-') - ord('0')
        else:
            tmp += int(i)

    return str(tmp)

if(len(n) == 1):
    print(1)
else:
    count=0
    while(len(n) != 1):
        count +=1
        n = sum(n)
    print(count)
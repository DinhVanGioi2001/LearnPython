test= int(input())
while(test):
    test -= 1
    n = int(input())
    line = input()
    list = line.split(" ")
    for i in range(0, n):
        list[i] = int(list[i])
    hash = dict()
    max, num = 0, 0
    for element in list:
        if element in hash:
            hash[element] += 1 # key     : vallue
        else:                  # element :
            hash[element] = 1
    for key in hash:
        if hash[key] > max:
            max = hash[key]
            num = key
    if(max > n/2):
        print(num)
    else:
        print("NO")
test = int(input())
while(test):
    test -= 1
    n = int(input())
    print("1 * ", end="")
    i = 2
    dem = 0
    while(n > 1):
        if n % i == 0:
            dem += 1
            if n == i:
                print(str(i) + '^' + str(dem), end="")
            n /= i
        else:
            if dem > 0:
                print(str(i) + '^' + str(dem) + ' * ', end="")
                dem = 0
            i += 1
    print("")
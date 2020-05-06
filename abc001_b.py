n = int(input())/10e2
if 0.1 > n:
    print("00")
elif 5 >= n:
    if len(str(int(n*10))) == 1:
        print("0{}".format(int(n*10)))
    else:
        print(int(n*10))
elif 30 >= n:
    print(int(n)+50)
elif 70 >= n:
    print((int(n) - 30)//5 + 80)
else:
    print(89)

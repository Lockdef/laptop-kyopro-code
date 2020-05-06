x, y = map(int, input().split())
a = abs(abs(x) - abs(y))
if x > -1 and y > -1:
    print(a)
elif x < 0 and y < 0:
    print(a + 2)
else:
    print(a + 1)

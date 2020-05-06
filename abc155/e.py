n = int(input())
s = 0
while n > 0:
    i = int(str(n)[0])
    if i > 5:
        n = 1 * 10 ** (len(str(n))) - n
        s += 1
    else:
        s += i
        n -= i * 10 ** (len(str(n)) - 1)

print(s)

S = input()
c = 0
start = 0
for s in S:
    if s == 'R':
        c += 1
        start = 1
    else:
        if start:
            break
print(c)

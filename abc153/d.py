h = int(input())
i = 1
a = 1
b = 1
c = 1

while h >= a:
    a = 2 ** i
    i += 1

s = 0
t = True
for j in range(1, i-1):
    c += 2 ** j

print(c)

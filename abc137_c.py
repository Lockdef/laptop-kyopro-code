from collections import Counter
s = [''.join(sorted(list(input()))) for i in range(int(input()))]
a = 0
t = []
for i in s:
    print(":::::::", i)
    if i in t:
        a += 1
    else:
        t.append(i)
print(a)

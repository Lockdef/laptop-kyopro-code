from collections import Counter
n = int(input())
s = [input() for _ in [0] * n]
s = Counter(s)
a = max(s.values())
b = s.most_common()[:list(s.values()).count(a)]
b = sorted(b, key=lambda x: x[0])
for i in b:
    print(i[0])

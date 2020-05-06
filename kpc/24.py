s = input()
s = sorted(s)
a = s.count("a")
b = s.count("b")
c = s.count("c")
d = max(a, b, c)
if d > len(s) / 2:
    print("NO")
else:
    print("YES")

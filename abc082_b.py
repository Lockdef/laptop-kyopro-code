s = input()
t = input()

a = "".join(sorted(s, reverse=True))
b = "".join(sorted(t))

if sorted([a, b])[0] == b:
    print("Yes")
else:
    print("No")
print(sorted([a, b]))

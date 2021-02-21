s = input()
for i in s[1::2]:
    if ord(i) > 90:
        print("No")
        exit()
for i in s[::2]:
    if ord(i) < 90:
        print("No")
        exit()
print("Yes")

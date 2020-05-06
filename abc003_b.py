s = input()
t = input()
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    elif s[i] == "@":
        if t[i] not in "atcoder":
            print("You will lose")
            break
    elif t[i] == "@":
        if s[i] not in "atcoder":
            print("You will lose")
            break
    else:
        print("You will lose")
        break
else:
    print("You can win")

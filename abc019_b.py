s = input()
r = [s[0]]
c = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        c += 1
    else:
        r.append(str(c))
        r.append(s[i])
        c = 1

print("".join(r)+str(c))

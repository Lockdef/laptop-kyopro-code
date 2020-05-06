s = input()
k = int(input())
t = []
c = 0
for i in range(len(s)):
    if len(s[i:i+k]) == k:
        if s[i:i+k] in t:
            continue
        else:
            t.append(s[i:i+k])
            c += 1
print(c)

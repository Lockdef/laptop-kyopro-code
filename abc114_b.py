s = input()
t = 100000000000
for i in range(len(s)-2):
    t = min(abs(753 - int(s[i]+s[i+1]+s[i+2])), t)
print(t)

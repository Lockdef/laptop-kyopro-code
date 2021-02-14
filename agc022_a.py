s = list(input())
if len(s) == 26:
    print(-1)
for i in range(26):
    if s.count(chr(97 + i)) == 0:
        print("".join(s) + chr(97 + i))
        break

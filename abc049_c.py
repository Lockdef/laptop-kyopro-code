s = list(input())[::-1]

c = 0

r = "YES"

while c < len(s):
    print(c, len(s))
    try:
        if s[c:c + 6] == list('eraser')[::-1]:
            c += 6
        elif s[c:c + 7] == list('dreamer')[::-1]:
            c += 7
        elif s[c:c + 5] == list('dream')[::-1] or s[c:c + 5] == list('erase')[::-1]:
            c += 5
        else:
            r = "NO"
            break
    except IndexError:
        r = "NO"
        break

print(r)

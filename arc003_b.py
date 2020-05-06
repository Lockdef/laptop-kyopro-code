n = int(input())
s = [input()[::-1] for _ in [0] * n]

s = sorted(s)

for i in s:
    print(i[::-1])

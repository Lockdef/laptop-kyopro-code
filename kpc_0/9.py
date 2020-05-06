n = int(input())
d = [int(input()) for _ in [0] * n]
print(len(set(sorted(d))))

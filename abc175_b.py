n = int(input())
lines = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x = lines[i]
            y = lines[j]
            z = lines[k]
            if x == y or y == z or x == z:
                continue
            a = (x + y) > z
            b = (x + z) > y
            c = (y + z) > x
            if a and b and c:
                count += 1

print(count)

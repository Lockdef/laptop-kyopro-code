from itertools import permutations
n, m = map(int, input().split())
edge = set()
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    edge.add((a, b))
    edge.add((b, a))
count = 0
p = list(permutations(list(range(n))))

for i in p:
    if i[0] != 0 ^ i[-1] != 0:
        continue
    for j in range(n - 1):
        x = i[j]
        y = i[j + 1]
        if (x, y) not in edge:
            break
    else:
        count += 1

print(count)

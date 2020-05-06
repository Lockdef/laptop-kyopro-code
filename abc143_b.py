import itertools as it

n = int(input())
d = map(int, input().split())

l = it.permutations(d, 2)

temp = 0

for i in l:
    temp += i[0] * i[1]

print(temp // 2)

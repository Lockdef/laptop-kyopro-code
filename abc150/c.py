from itertools import permutations

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

l = list(map(list, list(permutations(list(range(1, n+1)), n))))

print(abs(l.index(p)-l.index(q)))

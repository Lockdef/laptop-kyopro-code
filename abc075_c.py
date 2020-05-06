class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)
    def findroot(self, x):
        if (self.root[x] < 0):
            return x
        else:
            self.root[x] = self.findroot(self.root[x])
            return self.root[x]
    def unite(self, x, y):
        x = self.findroot(x)
        y = self.findroot(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] +=self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1
    def issamegroup(self, x, y):
        return self.findroot(x) == self.findroot(y)
    def count(self, x):
        return -self.root[self.findroot(x)]


N, M = map(int,input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

t = [[] for i in range(N+1)]

for a, b in ab:
    t[a].append(b)
    t[b].append(a)

c = 0

for i in t:
    if len(i) == 1:
        c += 1
    print(i)

print(c)

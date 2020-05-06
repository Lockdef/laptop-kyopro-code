N = int(input())
sp = [input().split() for i in range(N)]
sp = sorted(sp, reverse=True, key=lambda x: int(x[1]))
a = sum([int(i[1]) for i in sp]) / 2
if a < int(sp[0][1]):
    print(sp[0][0])
else:
    print("atcoder")

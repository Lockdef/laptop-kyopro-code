n = int(input())
a = list(map(int, input().split()))
s = 0  # aの累積和
ms = -float("inf")  # sの最大値
b = 0  # フェーズ開始時の座標
res = 0  # 結果
for i in range(n):
    s += a[i]
    ms = max(ms, s)
    res = max(res, b + ms)
    b += s
print(res)

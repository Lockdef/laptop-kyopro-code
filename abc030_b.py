n, m = map(int, input().split())
if m:
    md = m / 60 * 360
else:
    md = 0
if 0 < n <= 11:
    nd = n / 12 * 360 + md / 12
elif 12 < n:
    nd = (n - 12) / 12 * 360 + md / 12
else:
    nd = md / 12
s = abs(md - nd)
if s <= 180:
    print(s)
else:
    print(360 - s)

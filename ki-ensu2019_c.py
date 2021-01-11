n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = sorted([a[i] - b[i] for i in range(n)], reverse=True)
if sum(x) < 0:
    print(-1)
    exit()
minus_count = sum([1 if x[i] < 0 else 0 for i in range(n)])
if minus_count == 0:
    print(0)
    exit()
minus_sum = abs(sum([x[i] if x[i] < 0 else 0 for i in range(n)]))
count = minus_count
for i in range(n):
    if x[i] < 0:
        break
    minus_sum -= x[i]
    if minus_sum > -1:
        count += 1
    else:
        count += 1
        break
print(count)

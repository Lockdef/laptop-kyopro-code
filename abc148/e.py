N = int(input())



r = 0
for i in range(99):
    r += N // 10 // 5 ** i

print(r)

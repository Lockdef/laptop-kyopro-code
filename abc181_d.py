s = input()
hachi = set()
if len(s) < 3:
    if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
t = 104
while t < 1000:
    hachi.add(str(t))
    t += 8
counter = [0 for _ in range(10)]
for i in s:
    counter[int(i)] += 1
for h in hachi:
    count = [0 for _ in range(10)]
    for i in str(h):
        count[int(i)] += 1
    for i in range(10):
        if counter[i] < count[i]:
            break
    else:
        print("Yes")
        exit()
print("No")

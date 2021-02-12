n = int(input())
c = list(input())
d = []
for i in range(c.count("R")):
    d.append("R")
for i in range(c.count("W")):
    d.append("W")
count = {"R": 0, "W": 0}
for i in range(n):
    if c[i] != d[i]:
        count[d[i]] += 1
print(max(count.values()))

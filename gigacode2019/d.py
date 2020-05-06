h, w, k, v = map(int, input().split())

s = []

for i in range(h):
    s.append(list(map(int, input().split())))


def f(price_list):
    return sum(price_list) + (len(price_list) * k)


for i in range(h):

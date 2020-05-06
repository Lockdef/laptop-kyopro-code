from math import ceil
n = int(input())
a = map(int, input().split())
a = [i for i in a if i != 0]
print(ceil(sum(a) / len(a)))

x, y = map(int, input().split())

result = 0
if (x == 3):
    result += 100000
elif (x == 2):
    result += 200000
elif (x == 1):
    result += 300000


if (y == 3):
    result += 100000
elif (y == 2):
    result += 200000
elif (y == 1):
    result += 300000

if(result == 600000):
    result += 400000

print(result)

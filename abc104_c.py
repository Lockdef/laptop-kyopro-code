d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

min_count = float("inf")

for bit in range(2 ** d):
    count = 0
    point = 0
    problem = [int(pc[i][0]) for i in range(d)]
    for i in range(d):
        if bit & (1 << i):
            p = pc[i][0]
            c = pc[i][1]
            count += p
            point += 100 * (i + 1) * p + c
            problem[i] = 0

    while point < g:
        while point == 1300:
            pass
        for i in list(range(d))[::-1]:
            if problem[i] != 0:
                point += (i + 1) * 100
                count += 1
                problem[i] -= 1
                if problem[i] == 0:
                    point += pc[i][1]
                break

    min_count = min(min_count, count)

print(min_count)

xy = list(map(int, input().split()))
print(abs((xy[0] - xy[4]) * (xy[3] - xy[5]) -
          (xy[2] - xy[4]) * (xy[1] - xy[5])) / 2)

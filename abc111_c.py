from collections import Counter

n = int(input())
v = list(map(int, input().split()))

if len(set(v)) != 1:
    a = Counter(v[0::2]).most_common()
    b = Counter(v[1::2]).most_common()
    if a[0][0] != b[0][0]:
        print((len(v[0::2]) - a[0][1]) + (len(v[1::2]) - b[0][1]))
    else:
        if a[0][1] < b[0][1]:
            print((len(v[0::2]) - a[0][1]) + (len(v[1::2]) - b[1][1]))
        elif a[0][1] > b[0][1]:
            print((len(v[0::2]) - a[1][1]) + (len(v[1::2]) - b[0][1]))
        elif a[0][1] == b[0][1]:
            if len(a) != 1 and len(b) != 1:
                if a[1][1] > b[1][1]:
                    print((len(v[0::2]) - a[1][1]) + (len(v[1::2]) - b[0][1]))
                elif a[1][1] < b[1][1]:
                    print((len(v[0::2]) - a[0][1]) + (len(v[1::2]) - b[1][1]))
                elif a[1][1] == b[1][1]:
                    print((len(v[0::2]) - a[0][1]) + (len(v[1::2]) - b[1][1]))
            elif len(a) != 1:
                print((len(v[0::2]) - a[1][1]) + (len(v[1::2]) - b[0][1]))
            elif len(b) != 1:
                print((len(v[0::2]) - a[0][1]) + (len(v[1::2]) - b[1][1]))
else:
    print(len(v[1::2]))

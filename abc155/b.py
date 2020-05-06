n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i % 2 == 0:
        if i % 3 == 0 or i % 5 == 0:
            pass
        else:
            print("DENIED")
            break
else:
    print("APPROVED")

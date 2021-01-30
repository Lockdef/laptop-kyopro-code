a, b, c = map(int, input().split())
if a < b:
    print("Aoki")
elif a > b:
    print("Takahashi")
else:
    if c == 1:
        print("Takahashi")
    else:
        print("Aoki")

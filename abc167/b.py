A,B,C,K = map(int,input().split())
if K <= A:
    print(K * 1)
else:
    c = A * 1
    if K <= A + B:
        pass
    else:
        if K <= A + B + C:
            c += (K - A - B) * -1
        else:
            c += C * -1
    print(c)

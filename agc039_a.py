S = input()
K = int(input())
if len(set(S)) == 1:
    print(len(S) // 2 * K)
else:
    c = 0
    for i in range(0, len(S) - 1, 2):
        if S[i] == S[i + 1]:
            c += 1
    if S[0] == S[-1] or len(S) % 2 == 0:
        print(c * K)
    else:
        mn m
        a = 1
        b = 1
        for i in S[1:]:
            if i == S[0]:
                a += 1
            else:
                break
        for i in S[-2::-1]:
            if i == S[-1]:
                b += 1
            else:
                break
        print(c * K - (K - 1) * (a // 2 + b // 2 - (a + b) // 2))

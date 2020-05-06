S = input()
a = (len(S) - 1) // 2
b = (len(S) + 3) // 2 - 1
if S == S[::-1] and S[:a] == S[:a][::-1] and S[b:] == S[b:][::-1]:
    print("Yes")
else:
    print("No")

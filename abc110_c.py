S = input()
T = input()

start = [-1]*26
goal = [-1]*26

temp = 0

for i in range(len(S)):
    a = ord(S[i]) - ord("a")
    b = ord(T[i]) - ord("a")

    if (b in start or a in goal):
        if (start[a] != b or goal[b] != a):
            temp = 1
            break
    else:
        start[a] = b
        goal[b] = a

if temp:
    print("No")
else:
    print("Yes")

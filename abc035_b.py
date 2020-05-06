S = input()
T = input()
R = ["L", "R", "U", "D", "?"]
Q = [0, 0, 0, 0, 0]  # L, R, U, D, ?
for i in S:
    for j in range(5):
        if i == R[j]:
            Q[j] += 1
if T == "2":
    a = abs(Q[0] - Q[1])
    b = abs(Q[2] - Q[3])
    c = Q[4]
    if a + b >= c:
        print(a + b - c)
    else:
        if a + b % 2 == c % 2:
            print(0)
        else:
            print(1)
else:
    print(abs(Q[0] - Q[1]) + abs(Q[2] - Q[3]) + Q[4])

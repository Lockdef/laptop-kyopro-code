s = input()
for i in range(8):
    op = list("-".join(list(s)))
    for j in range(3):
        if i & (1 << j):
            op[j + j + 1] = '+'
    op = "".join(op)
    if eval(op) == 7:
        print(op + "=7")
        break

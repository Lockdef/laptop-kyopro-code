x = input()
t = False
for i in x:
    if i == 'h' and not t:
        print("NO")
        break
    if (t and i != 'h'):
        print("NO")
        break
    else:
        t = False
    if i not in "cohku":
        print("NO")
        break
    if i == 'c':
        t = True
else:
    print("YES")

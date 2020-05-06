s = input()
d = s.split("WW")

a = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]

if len(d[1]) == 5:
    print(a[2-d[0].count("W")])
else:
    print(a[5-d[0].count("W")])

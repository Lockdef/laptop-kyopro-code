s = int(input())
a = s//3600
s = s-a*3600
b = s//60
s = s-b*60
c = s
if
print("%02d:%02d:%02d" % (a, b, c))

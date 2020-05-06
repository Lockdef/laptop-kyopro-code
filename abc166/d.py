X = int(input())
for i in range(-122, 122):
    for j in range(i, 122):
        if j ** 5 - i ** 5 == X:
            print(j, i)
            exit()

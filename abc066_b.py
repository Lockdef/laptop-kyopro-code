S = input()

for i in range(1, len(S)):
    length = len(S) - i
    if length % 2:
        continue
    half = length // 2
    if S[:half] == S[half:length]:
        print(length)
        break

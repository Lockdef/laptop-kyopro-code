from queue import Queue
k = int(input())
q = Queue()
for i in range(9):
    q.put(i + 1)
for i in range(k):
    x = q.get()
    y = x % 10
    if x % 10 != 0:
        q.put(10 * x + y - 1)
    q.put(10 * x + y)
    if x % 10 != 9:
        q.put(10 * x + y + 1)
print(x)

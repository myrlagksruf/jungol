import sys
input = sys.stdin.readline
print = sys.stdout.write
s = set(range(2, 1000001))
for i in range(2, 1001):
    if i not in s:
        continue
    for j in range(i * 2, 1000001, i):
        s.discard(j)
s.discard(2)
arr = sorted(s)
while True:
    n = int(input())
    if n == 0:
        break
    for i in arr:
        if (n - i) not in s:
            continue
        print(f"{n} = {i} + {n - i}\n")
        break
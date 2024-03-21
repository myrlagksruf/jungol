import sys
input = sys.stdin.readline
print = sys.stdout.write
s = set(range(2, 1001))
for i in range(2, 1001):
    if i not in s:
        continue
    for j in range(i * 2, 1001, i):
        s.discard(j)

n = int(input())
count = 0
for i in input().split():
    if int(i) in s:
        count += 1

print(str(count))
import sys
input = sys.stdin.readline
print = sys.stdout.write
cur = 100
n = int(input())
m = int(input())

s = set(map(str,range(10)))
if m != 0:
    mList = { i for i in input().split() }
    s -= mList
mi = 1000000
for i in range(1000000):
    if i == 100:
        mi = min(mi, abs(n - 100))
        continue
    st = str(i)
    x = set(st)
    if not x <= s:
        continue
    mi = min(mi, len(st) + abs(n - i))

print(f"{mi}\n")
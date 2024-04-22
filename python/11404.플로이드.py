import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())

d = [[float('inf')] * n for _ in range(n)]
for i in range(n):
  d[i][i] = 0

for _ in range(m):
  s, e, t = map(int, input().split())
  if d[s - 1][e - 1] > t: d[s - 1][e - 1] = t

for md in range(n):
  for st in range(n):
    for ed in range(n):
      if d[st][ed] > d[st][md] + d[md][ed]:
        d[st][ed] = d[st][md] + d[md][ed]

print('\n'.join(' '.join(str(j if j != float('inf') else 0) for j in d[i]) for i in range(n)))
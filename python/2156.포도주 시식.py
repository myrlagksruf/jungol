import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

podos = []

for _ in range(n):
  podos.append(int(input()))

d = (0, podos[0], 0)

for i in range(1, n):
  d = max(d), d[0] + podos[i], d[1] + podos[i]

print(f"{max(d)}\n")
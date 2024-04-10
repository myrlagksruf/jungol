import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
from math import copysign
N, M, R = map(int, input().split())

arr = deque(deque(int(i) for i in input().split()) for _ in range(N))

cmds = [int(i) for i in input().split()]

def mul_matrix(a, b):
  arr = [0, 0]
  for i in range(2):
    for j in range(2):
      arr[i] += a[i][j] * b[j]
  return arr

NM, NN = M, N
for i in cmds:
  if i == 3 or i == 4:
    NM, NN = NN, NM

result = [[0] * NM for _ in range(NN)]

for i in range(N):
  for j in range(M):
    NM, NN = M, N
    p = [2 * j - M + 1, 2 * i - N + 1]
    for k in cmds:
      if k == 1:
        p[1] = -p[1]
      elif k == 2:
        p[0] = -p[0]
      elif k == 3:
        p[0], p[1] = -p[1], p[0]
        NM, NN = NN, NM
      elif k == 4:
        p[0], p[1] = p[1], -p[0]
        NM, NN = NN, NM
      elif k == 5:
        p = [
          p[0] - int(copysign(1, p[0]) * NM * int(p[0] * p[1] > 0)),
          p[1] - int(copysign(1, p[1]) * NN * int(p[0] * p[1] < 0))
        ]
      elif k == 6:
        p = [
          p[0] - int(copysign(1, p[0]) * NM * int(p[0] * p[1] < 0)),
          p[1] - int(copysign(1, p[1]) * NN * int(p[0] * p[1] > 0))
        ]
    p[0] = (p[0] + NM - 1) // 2
    p[1] = (p[1] + NN - 1) // 2
    result[p[1]][p[0]] = arr[i][j]

print('\n'.join(' '.join(map(str, i)) for i in result))
import sys
input = sys.stdin.readline
print = sys.stdout.write
from copy import deepcopy
from pprint import pprint

N, M, k = map(int, input().split())

arr = [[(int(i), k) for i in input().split()] for _ in range(N)]

way = [int(i) for i in input().split()]
way.insert(0, 0)

order = [[]]

for _ in range(M):
  shark_order = [[int(i) for i in input().split()] for _ in range(4)]
  shark_order.insert(0, [])
  order.append(shark_order)

way_map = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

def move_shark():
  new_arr = deepcopy(arr)
  for i in range(N):
    for j in range(N):
      elm = new_arr[i][j]
      if elm[0] == 0 or elm[1] != k:
        continue
      for w in order[elm[0]][way[elm[0]]][1:]:
        nx = i + way_map[way[elm[0]]][0] * w
        ny = j + way_map[way[elm[0]]][1] * w
        if 0 <= nx < N and 0 <= ny < N:
          if new_arr[nx][ny][0] == 0:
def check():
  pass

while True:
  pass
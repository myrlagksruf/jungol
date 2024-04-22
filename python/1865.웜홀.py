import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

for _ in range(int(input())):
  N, M, W = map(int, input().split())
  graph:dict[int,dict[int, int]] = { key:{} for key in range(1, N + 1)}
  for _ in range(M):
    S, E, T = map(int, input().split())
    if E not in graph[S] or graph[S][E] > T:
      graph[S][E] = T
    if S not in graph[E] or graph[E][S] > T:
      graph[E][S] = T
  for _ in range(W):
    S, E, T = map(int, input().split())
    if E not in graph[S] or graph[S][E] > -T:
      graph[S][E] = -T

  distance = [float('inf')] * (N + 1)
  visited:set[int] = set()
  flag = False
  for i in range(1, N + 1):
    if distance[i] != float('inf'):
      continue
    distance[i] = 0

    cur:set[int] = set([i])
    d = deque([(i, 0)])
    max_score = 0
    while len(d):
      node, score = d.popleft()
      for nn in graph[node].keys():
        if nn in cur or nn in visited:
          continue
        visited.add(nn)
        cur.add(nn)
        max_score = max(max_score, score + 1)
        d.append((nn, score + 1))

    # Relaxation 과정 (노드 수 - 1번 반복)
    for _ in range(len(cur)):
      for node in cur:
        for neighbor, val in graph[node].items():
          # 만약 이 경로를 통한 거리가 더 짧다면 업데이트
          if distance[node] + val < distance[neighbor]:
            distance[neighbor] = distance[node] + val

    # 음수 사이클 존재 여부 확인
    for node in cur:
      for neighbor, val in graph[node].items():
        if distance[node] + val < distance[neighbor]:
          flag = True
          break
      if flag:break
    if flag:break
  if flag:
    print("YES\n")
  else:
    print("NO\n")

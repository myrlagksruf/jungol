import sys
input = sys.stdin.readline
print = sys.stdout.write
from typing import Callable

class SegmentTree:
  n:int
  tree:list[int]
  op:Callable[[int, int], int]
  def __init__(self, data:list[int], op:Callable[[int, int], int]):
    self.n = len(data)
    self.tree = [0] * (2 * self.n)
    self.op = op
    self.build(data)

  def build(self, data:list[int]):
    # 리프 노드 초기화
    for i in range(self.n):
      self.tree[self.n + i] = data[i]

    # 내부 노드 초기화
    for i in range(self.n - 1, 0, -1):
      self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

  def update(self, pos:int, value:int):
    # 리프 노드 업데이트
    pos += self.n
    self.tree[pos] = value
    # 내부 노드 업데이트
    while pos > 1:
      pos //= 2
      self.tree[pos] = self.op(self.tree[2 * pos], self.tree[2 * pos + 1])

  def query(self, left, right, result = 0):
    # 구간 [left, right) 합 계산
    left += self.n
    right += self.n
    while left < right:
      if left % 2 == 1:
        result = self.op(result, self.tree[left])
        left += 1
      if right % 2 == 1:
        right -= 1
        result = self.op(result, self.tree[right])
      left //= 2
      right //= 2
    return result

N, M = map(int, input().split())

data = [int(input()) for _ in range(N)]
seg_tree_max = SegmentTree(data, max)
seg_tree_min = SegmentTree(data, min)

result = []

for _ in range(M):
  a, b = map(int, input().split())
  result.append(f"{seg_tree_min.query(a - 1, b, 1000000000)} {seg_tree_max.query(a - 1, b)}")

print('\n'.join(result))
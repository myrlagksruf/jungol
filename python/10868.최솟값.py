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
  

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]
seg = SegmentTree(data, min)
result:list[str] = []
for _ in range(m):
  a, b = map(int, input().split())
  result.append(f"{seg.query(a - 1, b, 10 ** 9 + 1)}")
  
print("\n".join(result))
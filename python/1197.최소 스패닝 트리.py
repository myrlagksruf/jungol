import sys
input = sys.stdin.readline
print = sys.stdout.write

class SimpleUnionFind:
  def __init__(self):
    self.parent = {}
  
  def find(self, x):
    if x not in self.parent:
      self.parent[x] = x
    if x != self.parent[x]:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
  
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x != root_y:
      self.parent[root_y] = root_x

V, E = map(int, input().split())

arr = [tuple(int(i) for i in input().split()) for _ in range(E)]

arr.sort(key=lambda v:v[2])
Varr:list[int] = [0] * (V + 1)
result = []
uf = SimpleUnionFind()
for a, b, c in arr:
  if Varr[a] == 0 and Varr[b] == 0:
    Varr[a] = 1
    Varr[b] = 1
    uf.union(a, b)
    result.append(c)
    continue
  if Varr[b] == 0 or Varr[a] == 0:
    Varr[b] = 1
    Varr[a] = 1
    uf.union(a, b)
    result.append(c)
    continue
  root_a = uf.find(a)
  root_b = uf.find(b)
  if root_a == root_b:
    continue
  uf.union(a, b)
  result.append(c)

print(f"{sum(result)}\n")
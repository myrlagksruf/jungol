import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 5)

N = int(input())
arr:list[dict[int, int]] = [{} for _ in range(N + 1)]
tree:list[set[int]] = [set() for _ in range(N + 1)]
deptharr:list[int] = [0] * (N + 1)
valuearr:list[int] = [0] * (N + 1)
partree = [[0] * 20 for _ in range(N + 1)]
twice = {1 << i:i for i in range(20)}
visited = set()
for _ in range(N - 1):
  a, b, v = map(int, input().split())
  arr[a][b] = v
  arr[b][a] = v

M = int(input())

def settree(par:int, depth:int, value:int = 0):
  visited.add(par)
  valuearr[par] = value
  deptharr[par] = depth
  for cha, v in arr[par].items():
    if cha in visited:
      continue
    tree[par].add(cha)
    partree[cha][0] = par
    for i in range(1, 20):
      partree[cha][i] = partree[partree[cha][i - 1]][i - 1]
      if partree[cha][i] == 0:
        break
    settree(cha, depth + 1, v + value)

settree(1, 0)

def LCA(oria: int, orib: int):
  a, b = oria, orib
  if deptharr[a] < deptharr[b]:
    a, b = b, a
  gap = deptharr[a] - deptharr[b]
  while gap:
    first = gap & (-gap)
    a = partree[a][twice[first]]
    gap -= first
  if a == b:
    return a
  if partree[a][0] == partree[b][0]:
    return partree[a][0]
  cur = 1
  while True:
    if partree[a][cur] != partree[b][cur]:
      cur += 1
      continue
    a = partree[a][cur - 1]
    b = partree[b][cur - 1]
    cur = 0
    if a == b:
      return a
    if partree[a][0] == partree[b][0]:
      return partree[a][0]
  

res:list[str] = []
for _ in range(M):
  a, b = map(int, input().split())
  # print(f"\n{a}, {b}, {valuearr[a]}, {valuearr[b]} : {LCA(a, b)}\n")
  res.append(f"{valuearr[a] + valuearr[b] - 2 * valuearr[LCA(a, b)]}")

print("\n".join(res))
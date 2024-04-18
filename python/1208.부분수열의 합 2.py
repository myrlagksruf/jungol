import sys
input = sys.stdin.readline
print = sys.stdout.write

N, S = map(int, input().split())

arr = sorted(map(int, input().split()))

adict = {}
bdict = {}

def dfs(cur:int, ed:int, acc:int, di:dict[int, int]):
  if ed == cur:
    di[acc] = di.get(acc, 0) + 1
    return
  dfs(cur + 1, ed, acc + arr[cur], di)
  dfs(cur + 1, ed, acc, di)

dfs(0, N // 2, 0, adict)
dfs(N // 2, N, 0, bdict)

adict[0] -= 1
bdict[0] -= 1

result = adict.get(S, 0) + bdict.get(S, 0)
for key, val in adict.items():
  result += bdict.get(S - key, 0) * val

print(f"{result}\n")
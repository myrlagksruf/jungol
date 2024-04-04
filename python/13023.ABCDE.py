import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 4)

N, M = map(int, input().split())

di = { n:set() for n in range(N) }

for _ in range(M):
    a, b = map(int, input().split())
    di[a].add(b)
    di[b].add(a)

visit = [False] * N
def dfs(n, d):
    global visit
    visit[n] = True
    ma = d
    for i in di[n]:
        if visit[i]:
            continue
        ma = max(dfs(i, d + 1), ma)
        if ma >= 4:
            return ma
    visit[n] = False
    return ma

for i in range(N):
    result = dfs(i, 0)
    if result >= 4:
        print("1\n")
        exit()
print("0\n")
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 5)
K = int(input())

def dfs(g, st, c, his):
    his.discard(st)
    for i in g[st]["E"]:
        if g[i]["C"] == -1:
            g[i]["C"] = 1 - c
        elif g[i]["C"] == c:
            return False
        elif g[i]["C"] == 1 - c:
            continue
        if not dfs(g, i, 1 - c, his):
            return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    di = { i: { "E":set(), "C":-1 } for i in range(1, V + 1) }
    for _ in range(E):
        V1, V2 = map(int, input().split())
        st = V1
        di[V1]["E"].add(V2)
        di[V2]["E"].add(V1)
    his = set(range(1, V + 1))
    while len(his):
        st = his.pop()
        if not dfs(di, st, 0, his):
            print("NO\n")
            break
    else:
        print("YES\n")
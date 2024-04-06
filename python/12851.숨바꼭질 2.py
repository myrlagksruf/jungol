import sys
input = sys.stdin.readline
print = sys.stdout.write
N, K = map(int, input().split())

def dfs(n, k):
    if n >= k:
        return (n - k, 2 if n == 2 and k == 1 else 1)
    if k == 1:
        return (1, 1)
    if k % 2 == 1:
        kp1 = dfs(n, k + 1)
        km1 = dfs(n, k - 1)
        if kp1[0] == km1[0]:
            return (kp1[0] + 1, kp1[1] + km1[1])
        mi = min(kp1, km1)
        return (mi[0] + 1, mi[1])
    kn = (k - n, 1)
    k2 = dfs(n, k // 2)
    k2 = (k2[0] + 1, k2[1])
    if kn[0] == k2[0]:
        return (kn[0], kn[1] + k2[1])
    return min(kn, k2)

print('\n'.join(map(str,dfs(N, K))))
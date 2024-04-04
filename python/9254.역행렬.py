import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [[int(i) for i in input().split()] for _ in range(n)]

def get_inv(arr):
    inv = [[int(i == j) for i in range(n)] for j in range(n)]
    for i in range(n):
        if abs(arr[i][i]) < sys.float_info.epsilon:
            for j in range(i + 1, n):
                if abs(arr[j][i]) < sys.float_info.epsilon:
                    continue
                arr[i], arr[j] = arr[j], arr[i]
                inv[i], inv[j] = inv[j], inv[i]
                break
            else:
                return "no inverse"
        
        pi = arr[i][i]
        for j in range(n):
            arr[i][j] /= pi
            inv[i][j] /= pi

        for j in range(n):
            if i == j:
                continue
            fac = arr[j][i]
            for k in range(n):
                arr[j][k] -= fac * arr[i][k]
                inv[j][k] -= fac * inv[i][k]
    return '\n'.join(' '.join(map(lambda v: str(v), i)) for i in inv)

print(f"{get_inv(arr)}\n")
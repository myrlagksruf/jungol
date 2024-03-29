import sys
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())

arr = [[0] * 3 for _ in range(max(4, n + 1))]
arr[1][0] = 1
arr[2][0] = 1
arr[2][1] = 1
arr[3][0] = 2
arr[3][1] = 1
arr[3][2] = 1

for i in range(4, n + 1):
    arr[i][0] = sum(arr[i - 1])
    arr[i][1] = sum(arr[i - 2])
    arr[i][2] = sum(arr[i - 3])

if sum(arr[n]) < k:
    print("-1\n")
    exit()

result = []
cur = n
while cur > 0:
    for j in range(3):
        if k <= arr[cur][j]:
            cur -= j + 1
            result.append(j + 1)
            break
        k -= arr[cur][j]
    else:
        v = n - sum(result)
        if v != 0:
            result.append(v)
        break

print(f"{'+'.join(map(str,result))}\n")

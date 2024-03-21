import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().rstrip()))

def checkcol(arr, ind):
    m = 0
    cur = ''
    curm = 0
    for i in range(len(arr)):
        if cur == arr[ind][i]:
            curm += 1
        else:
            cur = arr[ind][i]
            curm = 1
        m = max(m, curm)
    return m

def checkrow(arr, ind):
    m = 0
    cur = ''
    curm = 0
    for i in range(len(arr)):
        if cur == arr[i][ind]:
            curm += 1
        else:
            cur = arr[i][ind]
            curm = 1
        m = max(m, curm)
    return m

def swap(arr, tu1, tu2):
    temp = arr[tu1[0]][tu1[1]]
    arr[tu1[0]][tu1[1]] = arr[tu2[0]][tu2[1]]
    arr[tu2[0]][tu2[1]] = temp

m = 0
for i in range(len(arr)):
    temp = checkcol(arr, i)
    m = max(m, temp)

way = [(1, 0), (0, 1)]

for i in range(n):
    for j in range(n):
        for di, dj in way:
            if i + di >= len(arr) or j + dj >= len(arr):
                continue
            swap(arr, (i, j), (i + di, j + dj))
            result = []
            result.append(checkcol(arr, i))
            if i + di != i:
                result.append(checkcol(arr, i + di))
            result.append(checkrow(arr, j))
            if j + dj != j:
                result.append(checkrow(arr, j + dj))
            swap(arr, (i, j), (i + di, j + dj))
            result.append(m)
            m = max(result)

print(f"{m}\n")
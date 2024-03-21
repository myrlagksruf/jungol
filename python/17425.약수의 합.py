import sys
input = sys.stdin.readline
print = sys.stdout.write
arr = [1] * 1000001
for i in range(2, 1000001):
    for j in range(i, 1000001, i):
        arr[j] += i
for i in range(2, 1000001):
    arr[i] = arr[i] + arr[i - 1]
n = int(input())
printArr = []
for i in range(n):
    printArr.append(str(arr[int(input())]))
print('\n'.join(printArr))
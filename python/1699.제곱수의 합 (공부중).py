import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

arr = [0] * (n + 1)

for i in range(1, n + 1):
    arr[i] = arr[i - 1] + 1
    j = 2
    while i - j * j >= 0:
        arr[i] = min(arr[i - j * j] + 1, arr[i])
        j += 1

print(f"{arr[n]}\n")

# ??????????
# def solve(n):

#     if n == 0: return 0
#     if n == int(n ** 0.5) ** 2: return 1

#     while n % 4 == 0 and n > 0: n //= 4
#     if n % 8 == 7: return 4

#     for i in range(1, int((n/2) ** 0.5) + 1):
#         if i ** 2 + int((n - i**2) ** 0.5) ** 2 == n:
#             return 2
    
#     return 3
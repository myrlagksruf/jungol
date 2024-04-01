import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
N = 9901

b0 = 1
b1 = 2

for i in range(n - 1):
  b0, b1 = (b0 + b1) % N, (2 * b0 + b1) % N

print(f"{(b0 + b1) % N}\n") 
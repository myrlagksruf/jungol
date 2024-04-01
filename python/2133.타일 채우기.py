import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

if n % 2 == 1:
  print("0\n")
  exit()

n //= 2

a = 1
b = 3

for i in range(n - 1):
  a, b = b, 4 * b - a

print(f"{b}\n")
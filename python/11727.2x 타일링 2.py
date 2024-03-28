import sys
input = sys.stdin.readline
print = sys.stdout.write

a = 1
b = 1

for i in range(int(input()) - 1):
    a, b = b, (2 * a + b) % 10007

print(f"{b}\n")
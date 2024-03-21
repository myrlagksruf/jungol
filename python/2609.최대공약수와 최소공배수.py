from math import gcd
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
g = gcd(n, m)
print(f"{g}\n{n * m // g}")
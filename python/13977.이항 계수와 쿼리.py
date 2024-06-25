import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
P = 1000000007
def extended_gcd(a, b):
  if a == 0:
    return b, 0, 1
  g, x1, y1 = extended_gcd(b % a, a)
  x = y1 - (b // a) * x1
  y = x1
  return g, x, y

def mod_inverse_extended_gcd(a, m):
  g, x, _ = extended_gcd(a, m)
  if g != 1:
    raise ValueError(f"No modular inverse exists for {a} and {m}")
  return x % m

factorial = [1] * 4000001
for i in range(1, 4000001):
  factorial[i] = i * factorial[i - 1] % P

for _ in range(N):
  n, r = map(int, input().split())
  first = factorial[n] * mod_inverse_extended_gcd(factorial[r], P) % P
  second = first * mod_inverse_extended_gcd(factorial[n - r], P) % P
  print(f"{second}\n")
import sys
input = sys.stdin.readline

def check(n:int):
    r = 1 % n
    count = 1
    while True:
        if r == 0:
            return count
        r = (r * 10 + 1) % n
        count += 1

try:
    while True:
        num = int(input())
        print(check(num))
except:
    exit()
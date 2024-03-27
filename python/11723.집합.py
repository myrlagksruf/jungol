import sys
input = sys.stdin.readline
print = sys.stdout.write

m = int(input())
s = 0

di = {
    "add":lambda s, a: s | (1 << a),
    "remove":lambda s, a: s & ~(1 << a),
    "check":lambda s, a: int((s & (1 << a)) != 0),
    "toggle":lambda s, a: s ^ (1 << a),
    "all":lambda: (1 << 20) - 1,
    "empty":lambda: 0,
}

for _ in range(m):
    cmd = input().rstrip().split()
    if len(cmd) == 1:
        s = di[cmd[0]]()
        continue
    if cmd[0] == 'check':
        print(f"{str(di[cmd[0]](s, int(cmd[1]) - 1))}\n")
        continue
    s = di[cmd[0]](s, int(cmd[1]) - 1)
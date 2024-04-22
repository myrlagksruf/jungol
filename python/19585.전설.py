import sys
input = sys.stdin.readline
print = sys.stdout.write

triecolor = {}
C, N = map(int, input().split())
for _ in range(C):
  cur = triecolor
  color = input().rstrip()
  for i in color:
    if i not in cur:
      cur[i] = {}
    cur = cur[i]
  MAXC = max(MAXC, len(color))
  cur['A'] = True

names = set(input().rstrip() for _ in range(N))

Q = int(input())

def check_team(team:str):
  global triecolor, names
  cur = triecolor
  for i in range(min(len(team), 1000)):
    if team[i] not in cur:
      break
    cur = cur[team[i]]
    if 'A' in cur and team[i + 1:] in names:
      return 'Yes'
  return 'No'
      
for _ in range(Q):
  print(f"{check_team(input().rstrip())}\n")
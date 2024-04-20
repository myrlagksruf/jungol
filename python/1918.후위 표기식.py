import sys
input = sys.stdin.readline
print = sys.stdout.write

result = []
stack = []
op = '+-*/()'
br = '()'
oponly = '+-*/'
fastop = '*/'
slowop = '+-'

def allpop(check=False):
  global stack, result
  temp = []
  while len(stack):
    p = stack.pop()
    if p == '|':
      if check:
        stack.append('|')
      break
    if p in fastop:
      result.append(p)
    else:
      temp.append(p)
  result.append(''.join(temp))

for i in input().rstrip():
  if i not in op:
    result.append(i)
    continue
  if i == '(':
    stack.append('|')
    continue
  elif i == ')':
    allpop()
    continue
  if i in slowop: 
    allpop(True)
  elif len(stack) and stack[-1] in fastop:
    result.append(stack.pop())
  stack.append(i)

allpop()

print(f"{''.join(result)}\n")
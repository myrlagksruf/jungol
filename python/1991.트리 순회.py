import sys
input = sys.stdin.readline
print = sys.stdout.write


graph = {chr(i + 65):{"l":".", "r":"."} for i in range(26)}

for _ in range(int(input())):
  p, l, r = input().rstrip().split()
  graph[p]["l"] = l
  graph[p]["r"] = r

def preorder(node:str, arr:list[str]):
  if node == '.': return
  arr.append(node)
  preorder(graph[node]["l"], arr)
  preorder(graph[node]["r"], arr)
  return ''.join(arr)

def inorder(node:str, arr:list[str]):
  if node == '.': return
  inorder(graph[node]["l"], arr)
  arr.append(node)
  inorder(graph[node]["r"], arr)
  return ''.join(arr)

def postorder(node:str, arr:list[str]):
  if node == '.': return
  postorder(graph[node]["l"], arr)
  postorder(graph[node]["r"], arr)
  arr.append(node)
  return ''.join(arr)

print(f"{preorder('A', [])}\n")
print(f"{inorder('A', [])}\n")
print(f"{postorder('A', [])}\n")
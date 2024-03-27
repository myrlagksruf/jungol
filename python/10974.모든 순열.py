from itertools import *
print('\n'.join(map(lambda v:' '.join(map(str,v)),permutations(range(1,(r:=int(input()))+1),r))))
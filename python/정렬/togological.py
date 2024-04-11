from graphlib import TopologicalSorter

graph = {1: {2, 3}, 2: {3}, 4:set()}
ts = TopologicalSorter(graph)
print(tuple(ts.static_order()))

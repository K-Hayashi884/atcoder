import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n, m = list(map(int, input().split()))
edge = []
for i in range(m):
    edge.append(list(input().split()))
for i in range(n):
    edge.append([i+1, i+1])
edge = np.array(edge, dtype = np.int64).T
graph = csr_matrix(([1]*(m+n), (edge[:2] - 1)), (n, n))

cnt = 0
for i in range(n):
    ans = dijkstra(graph, directed=True, unweighted=True, indices=i-1)
    cnt += len([item for item in ans if item != np.inf])
print(cnt)
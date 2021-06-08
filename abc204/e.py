import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

n, m = list(map(int, input().split()))
edges = [list(map(int, input().split())) for i in range(m)]
weight = np.full(m, np.inf)

for i in range(m):
    tmp = edges[i][3]
    t = 1
    while t+int(edges[i][3]/(1+t)) < tmp:
        tmp = t+int(edges[i][3]/(1+t))
    weight[i] = tmp + edges[i][2]

edges = np.array(edges, dtype = np.int64)
print(weight)
print(edges[:, 0:2].T - 1)
graph = csr_matrix((weight, edges[:, 0:2].T - 1), (n, n))
print(graph)
ans = shortest_path(graph, directed=False, unweighted=False)
print(ans)
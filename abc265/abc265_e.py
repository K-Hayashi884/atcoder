import numpy as np
n, m = list(map(int, input().split()))
a, b, c, d, e, f = list(map(int, input().split()))
dp = np.zeros([n, 2*10**9+1, 2*10**9+1])
for _ in range(m):
    obstacle = list(map(int, input().split()))
    for i in range(n):
        dp[i][obstacle[0]][obstacle[1]] = -1

for i in range(n)

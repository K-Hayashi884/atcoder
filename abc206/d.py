import numpy as np

n = int(input())
a = list(map(int, input().split()))

dp = np.zeros((n, n))
his = []
for i in range(int(n/2)):
    s = a[i]
    b = a[-1-i]
    if s != b:
        dp[s-1][b-1] = 1
        dp[b-1][s-1] = 1
cnt = 0
while np.count_nonzero(dp) != 0:
    
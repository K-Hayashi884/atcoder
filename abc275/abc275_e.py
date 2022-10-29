n, m, k = list(map(int, input().split()))

dp = [[0]*n for _ in range(k)]
for i in range(m):
    dp[0][i] = 1

for i in range(1, k):
    for j in range(n-1):
        if dp[i-1][j] != 0:
            for l in range(1, m+1):
                if j+l<n:
                    dp[i][j+l] += dp[i-1][j]
                else:
                    dp[i][(n-1)+(-j-l+n-1)] += dp[i-1][j]

y = 0
for i in range(1,k+1):
    y += dp[i-1][-1]*(m**(k-i))
x = m**k
p = 998244353
ans = y%p
X = 1
n = p-2
while n>0:
    if (n & 1):
        X = X*x%p
    x = x*x%p
    n >>= 1
print(ans*X%p)
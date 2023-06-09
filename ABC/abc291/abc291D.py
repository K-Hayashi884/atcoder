n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0] for _ in range(n)]  # dp[i][flag]=i枚目まで条件を満たしている並べ方の数
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, n):
    for pre in (0, 1):
        for now in (0, 1):
            if ab[i - 1][pre] != ab[i][now]:
                dp[i][now] += dp[i - 1][pre]
    dp[i][0] %= 998244353
    dp[i][1] %= 998244353

print(sum(dp[n - 1]) % 998244353)

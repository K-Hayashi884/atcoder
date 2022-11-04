n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

dp = [[-300000]*n for _ in range(m)]
mm = a[0]
dp_m = [[-300000]*n for _ in range(m)]
for j in range(n):
    if a[j] > mm:
        mm = a[j]
    dp[0][j] = mm    
    dp_m[0][j] = mm  

for i in range(1, m):
    for j in range(i, n):
        if j == i:
            dp[i][j] = sum([a[k-1]*k for k in range(1, j+2)])
            dp_m[i][j] = sum([a[k-1]*k for k in range(1, j+2)])
            continue
        else:
            mm = dp_m[i-1][j-1] + a[j]*(i+1)
            if dp_m[i][j-1] > mm:
                dp[i][j] = dp_m[i][j-1]
                dp_m[i][j] = dp_m[i][j-1]
            else:
                dp[i][j] = mm
                dp_m[i][j] = mm

print(dp[-1][-1])
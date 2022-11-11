n, m = list(map(int, input().split()))
a, b, c, d, e, f = list(map(int, input().split()))
obs = set()
for _ in range(m):
    ob = input().split()
    obs.add(ob[0]+","+ob[1])

ans = 3**n
from collections import defaultdict
dp = [defaultdict(lambda: defaultdict(lambda: 0)) for _ in range(n+1)]
dp[0][0][0] += 1
for i in range(1, n+1):
    history = dp[i-1]
    for x, ys in history.items():
        for y, cnt in ys.items():
            if str(x+a)+","+str(y+b) in obs:
                ans -= 3**(n-i)
            else:
                dp[i][x+a][y+b] += cnt

            if str(x+c)+","+str(y+d) in obs:
                ans -= 3**(n-i)
            else:
                dp[i][x+c][y+d] += cnt

            if str(x+e)+","+str(y+f) in obs:
                ans -= 3**(n-i)
            else:
                dp[i][x+e][y+f] += cnt

print(ans%998244353)
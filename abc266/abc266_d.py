from collections import deque

n = int(input())
t = deque()
x = deque()
a = deque()
for _ in range(n):
    ti, xi, ai = list(map(int, input().split()))
    t.append(ti)
    x.append(xi)
    a.append(ai)

T = t[-1]
dp = [[-1]*(5) for _ in range(T+1)]
dp[0][0] = 0

for i in range(1, T+1):
    for j in range(5):
        if len(t) > 0  and t[0] < i:
            t.popleft()
            x.popleft()
            a.popleft()
        if j != 0 and dp[i-1][j-1] == -1:
            break
        
        if j == 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j+1])
        elif j == 4:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])

        if len(t) > 0  and t[0] == i:
            if x[0] == j:
                dp[i][j] += a.popleft()
                t.popleft()
                x.popleft()

print(max(dp[-1]))
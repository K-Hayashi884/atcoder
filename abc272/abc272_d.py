import math

n, m = list(map(int, input().split()))

dp = [[-1]*n for _ in range(n)]
dp[0][0] = 0

kl = []
for i in range(int(math.sqrt(m))+1):
    if math.sqrt(m-i**2).is_integer():
        kl.append([i, int(math.sqrt(m-i**2))])

newbie = [[0,0]]
cnt = 1
while newbie:
    next_newbie = []
    for p in newbie:
        for q in kl:
            x = p[0]+q[0]
            y = p[1]+q[1]
            if x<n and y<n and dp[x][y]==-1:
                dp[x][y] = cnt
                next_newbie.append([x, y])
            y = p[1]-q[1]
            if x<n and y>-1 and dp[x][y]==-1:
                dp[x][y] = cnt
                next_newbie.append([x, y])
            x = p[0]-q[0]
            if x>-1 and y>-1 and dp[x][y]==-1:
                dp[x][y] = cnt
                next_newbie.append([x, y])
            y = p[1]+q[1]
            if x>-1 and y<n and dp[x][y]==-1:
                dp[x][y] = cnt
                next_newbie.append([x, y])
    newbie = next_newbie
    cnt += 1

for i in range(n):
    print(*dp[i])
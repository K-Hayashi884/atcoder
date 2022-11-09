h, w = list(map(int, input().split()))
c = []
s = []
n_of_walls = 0
for i in range(h):
    tmp = input()
    c.append(tmp)
    if "S" in tmp:
        s = [i, tmp.index("S")]
    for j in tmp:
        if j == "#":
            n_of_walls += 1

def dfs(coords, dp, n_of_non_negas, n_of_odds):
    if c[coords[0]][coords[1]] == "#" or dp[coords[0]][coords[1]] > -1:
        return False
    dp[coords[0]][coords[1]] = 0

    flagged_nears = []
    if coords[0] != 0:
        flagged_nears.append([coords[0]-1, coords[1]])
    if coords[0] != h-1:
        flagged_nears.append([coords[0]+1, coords[1]])
    if coords[1] != 0:
        flagged_nears.append([coords[0], coords[1]-1])
    if coords[1] != w-1:
        flagged_nears.append([coords[0], coords[1]+1])

    for near in flagged_nears:
        if dp[near[0]][near[1]] > -1:
            dp[near[0]][near[1]] += 1
            dp[coords[0]][coords[1]] += 1
            if dp[near[0]][near[1]] % 2 == 0:
                n_of_odds -= 1
            else:
                n_of_odds += 1
            flagged_nears.remove(near)

    if dp[coords[0]][coords[1]]%2 == 1:
        n_of_odds += 1
    n_of_non_negas += 1
    if n_of_odds == 0 and n_of_non_negas > 3:
        for i in range(h):  
            print(dp[i])
        return True

    for near in flagged_nears:
        if dfs(near, dp, n_of_non_negas, n_of_odds):
            return True
    return False

dp = [[-1]*w for _ in range(h)]
if dfs(s, dp, 0, 0):
    print("Yes")
else:
    print("No")
    
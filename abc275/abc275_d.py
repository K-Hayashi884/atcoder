dp = dict()

def f(k):
    if k == 0:
        return 1
    elif k in dp:
        return dp[k]
    else:
        dp[k] = f(int(k/2))+f(int(k/3))
        return dp[k]

n = int(input())
print(f(n))
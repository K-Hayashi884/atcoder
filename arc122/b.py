n = int(input())
a = list(map(int, input().split()))

ans = sum(a)/n
a.sort()
for i in range(1, n):
    tmp = (sum(a) - sum(a[:i]) - a[i]*(n-i))/n + a[i]/2
    if tmp < ans:
        ans = tmp
print(ans)

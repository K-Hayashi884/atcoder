n = int(input())
t = list(map(int, input().split()))

dp = {0, t[0]}
for i in range(1, n):
    dp = dp.union({item+t[i] for item in dp})
print(min([item for item in dp if item >= sum(t)/2]))
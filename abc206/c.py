import collections

n = int(input())
a = list(map(int, input().split()))

cnt = [v for k, v in collections.Counter(a).items() if v > 1]
ans = int(n*(n-1)/2)
for c in cnt:
    ans -= int((c-1)*c/2)
print(ans)
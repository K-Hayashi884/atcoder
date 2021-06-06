h, w = list(map(int, input().split()))
s = []
for i in range(h):
    s.append(list(input()))

ans = 1
for i in range(h+w-1):
    li = []
    y = i if i <= h-1 else h-1
    x = i - y
    while x <= w-1 and  y >= 0 and x >= 0:
        li.append(s[y][x])
        y -= 1
        x += 1

    if 'B' in li and 'R' in li:
        print(0)
        exit()
    elif 'B' not in li and 'R' not in li:
        ans *= 2
print(ans % 998244353)
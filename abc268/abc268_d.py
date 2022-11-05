def dfs(t, l):
    if len(l) == 1:
        return l[0] == t
    elif len(l) == 0:
        return False
    mid = int(len(l)/2)
    if l[mid] == t:
        return True
    elif l[mid] < t:
        return dfs(t, l[mid+1:])
    else:
        return dfs(t, l[:mid])

from itertools import permutations, product
import sys
sys.setrecursionlimit(10 ** 9)

n, m = list(map(int, input().split()))
s = []
t = []
for _ in range(n):
    s.append(input())
for _ in range(m):
    t.append(input())

if n == 1:
    if s[0] in t:
        print(-1)
        exit()
    else:
        print(s[0])
        exit()

n_underbar = 16-(n-1)
for e in s:
    n_underbar -= len(e)
if n_underbar < 0:
    print(-1)
    exit()

t_int = []

for e in t:
    tmp = ""
    flg = True
    while len(e) > 0:
        i = 0
        while i < len(e)-1 and e[i+1] != "_":
            i += 1
        if e[:i+1] in s:
            tmp += str(s.index(e[:i+1])+1)
            e = e[i+1:]
        else:
            flg = False
            break
        if len(e) > 0:
            i = 0
            while e[i+1] == "_":
                i += 1
            tmp += str(i+1)
            e = e[i+1:]
    if flg:
        t_int.append(int(tmp))
t_int.sort()

s_indexes = list(permutations([str(i) for i in range(1, n+1)]))
underbar_indexes = list(product(range(n), repeat=n_underbar))
for i in range(len(s_indexes)):
    for j in range(len(underbar_indexes)):
        t = ""
        s_index = s_indexes[i]
        underbar_index = [1]*(n-1)
        for index in underbar_indexes[j]:
            if index < n-1:
                underbar_index[index] += 1
        for k in range(n-1):
            t += s_index[k]
            t += str(underbar_index[k])
        t += s_index[len(s_index)-1]
        if not dfs(int(t), t_int):
            ans = ""
            for k in range(n-1):
                ans += s[int(s_index[k])-1]
                ans += "_" * underbar_index[k]
            ans += s[int(s_index[len(s_index)-1])-1]
            print(ans)
            exit()

print(-1)


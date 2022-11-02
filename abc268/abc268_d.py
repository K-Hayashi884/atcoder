from collections import defaultdict

n, m = list(map(int, input().split()))
s = []
t = []
for _ in range(n):
    s.append(int(input()))
for _ in range(m):
    t.append(int(input()))

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

class recursivedefaultdict(defaultdict):
    def __init__(self):
        self.default_factory = type(self)

d = recursivedefaultdict()
for e in s:
    i = 0
    tmp = d
    while i < len(e)-1:
        while i < len(e) and e[i+1] != "_":
            i += 1
        if 

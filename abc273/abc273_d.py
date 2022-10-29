import bisect
from collections import defaultdict

h, w, rs, cs = list(map(int, input().split()))
n = int(input())
wall_r = defaultdict(lambda: [0, h+1])
wall_c = defaultdict(lambda: [0, w+1])

for i in range(n):
    r, c = list(map(int, input().split()))
    wall_r[c].append(r)
    wall_c[r].append(c)

for k in wall_r.keys():
    wall_r[k].sort()
for k in wall_c.keys():
    wall_c[k].sort()

# print(wall_r)
# print(wall_c)

q = int(input())

for i in range(q):
    d, l = input().split()
    l = int(l)
    if d == "U":
        wall = wall_r[cs][bisect.bisect_right(wall_r[cs], rs)-1]
        rs = rs-l if rs-l>wall else wall+1
    elif d == "D":
        wall = wall_r[cs][bisect.bisect_left(wall_r[cs], rs)]
        rs = rs+l if rs+l<wall else wall-1
    elif d == "R":
        wall = wall_c[rs][bisect.bisect_left(wall_c[rs], cs)]
        cs = cs+l if cs+l<wall else wall-1
    elif d == "L":
        wall = wall_c[rs][bisect.bisect_right(wall_c[rs], cs)-1]
        cs = cs-l if cs-l>wall else wall+1
    print(rs, cs)
import time

h, w, rs, cs = list(map(int, input().split()))
n = int(input())
wall_r = [[0, h+1] for _ in range(w)]
wall_c = [[0, w+1] for _ in range(h)]

for i in range(n):
    r, c = list(map(int, input().split()))
    wall_r[c-1].append(r)
    wall_c[r-1].append(c)

for wall in wall_r:
    wall.sort()
for wall in wall_c:
    wall.sort()

q = int(input())

def lower_bound(l, t):
    i = 0
    j = len(l)-1
    while i != j:
        if j-i == 1 and l[i] < t and l[j] > t:
            return l[i]
        mid = int((i+j)/2)
        if l[mid] == t:
            return l[mid-1]
        elif l[mid] > t:
            j = mid
        else:
            i = mid
    return l[i]
    
def upper_bound(l, t):
    i = 0
    j = len(l)-1
    while i != j:
        if j-i == 1 and l[i] < t and l[j] > t:
            return l[j]
        mid = int((i+j)/2)
        if l[mid] == t:
            return l[mid+1]
        elif l[mid] > t:
            j = mid
        else:
            i = mid
    return l[i]

for i in range(q):
    d, l = input().split()
    l = int(l)
    if d == "U":
        w = lower_bound(wall_r[cs-1], rs)
        rs = rs-l if rs-l>w else w+1
    elif d == "D":
        w = upper_bound(wall_r[cs-1], rs)
        rs = rs+l if rs+l<w else w-1
    elif d == "R":
        w = upper_bound(wall_c[rs-1], cs)
        cs = cs+l if cs+l<w else w-1
    elif d == "L":
        w = lower_bound(wall_c[rs-1], cs)
        cs = cs-l if cs-l>w else w+1
    print(rs, cs)
h, w, rs, cs = list(map(int, input().split()))
n = int(input())
wall_r = [[-1, w+1]]*h
wall_c = [[-1, h+1]]*w

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
            i = mid
        else:
            j = mid
    return l[i]

for i in range(q):
    d, l = input().split()
    l = int(l)
    if d == "D":
        w = lower_bound(wall_r[cs-1], rs)
        rs = rs-l if rs-l>w else w+1
        print(wall_r[cs-1])
    elif d == "U":
        w = upper_bound(wall_r[cs-1], rs)
        rs = rs+l if rs+l<w else w-1
        print(wall_r[cs-1])
    elif d == "R":
        w = upper_bound(wall_c[rs-1], cs)
        cs = cs+l if cs+l<w else w-1
        print(wall_c[rs-1])
    elif d == "L":
        w = lower_bound(wall_c[rs-1], cs)
        cs = cs-l if cs-l>w else w+1
        print(wall_c[rs-1])
    print(rs, cs)
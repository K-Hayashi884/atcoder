n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))

lo = [0]*10
le = [0]*10
for index, i in enumerate(a[1:]):
    if index%2 == 0:
        le[i-1] += 1
    else:
        lo[i-1] += 1

def dfs_e(s, d):
    if le[d-1] == 0:
        if d == 10:
            return s == y
        else:
            return dfs_e(s, d+1)
    else:
        if d == 10:
            for i in range(le[9]):
                if s+(10*i)+((-10)*(le[9]-i)) == y:
                    return True
                else:
                    return False
        else:
            for i in range(le[d-1]+1):
                if dfs_e(s+(d*i)+((-d)*(le[d-1]-i)), d+1):
                    return True
            return False

def dfs_o(s, d):
    if lo[d-1] == 0:
        if d == 10:
            return s == x
        else:
            return dfs_o(s, d+1)
    else:
        if d == 10:
            for i in range(lo[9]):
                if s+(10*i)+((-10)*(lo[9]-i)) == x:
                    return True
                else:
                    return False
        else:
            for i in range(lo[d-1]+1):
                if dfs_o(s+(d*i)+((-d)*(lo[d-1]-i)), d+1):
                    return True
            return False

flg_e = dfs_e(0, 1)
if flg_e:
    if dfs_o(a[0], 1):
        print("Yes")
    else:
        print("No")
else:
    print("No")


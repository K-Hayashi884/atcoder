n = int(input())

a = 1
b = n
c = 1
d = n
cnt_x = -1
cnt_y = -1

while cnt_x != 0:
    mid = int((a+b)/2)
    print("?", a, mid, 1, n)
    t = int(input())
    if t > cnt_x - t:
        cnt_x -= t
        a = mid+1
    else:
        cnt_x = t
        b = mid

while cnt_y != 0:
    mid = int((c+d)/2)
    print("?", a, b, c, mid)
    t = int(input())
    if t > cnt_y - t:
        cnt_y -= t
        c = mid+1
    else:
        cnt_y = t
        d = mid

print('!', int((a+b)/2), int((c+d)/2))
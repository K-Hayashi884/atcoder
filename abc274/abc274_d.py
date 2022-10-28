n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))

dp_x = [False] * (2*n*10+1)
dp_x[n*10] = True
dp_y = [False] * (2*n*10+1)
dp_y[n*10] = True

for index, ai in enumerate(a):
    if index%2 == 0:
        dp_x_tmp = [False] * (2*n*10+1)
        for i in range(2*n*10+1):
            if dp_x[i]:
                dp_x_tmp[i+ai] = True
                if index > 1:
                    dp_x_tmp[i-ai] = True
        dp_x = dp_x_tmp
    else:
        dp_y_tmp = [False] * (2*n*10+1)
        for i in range(2*n*10+1):
            if dp_y[i]:
                dp_y_tmp[i+ai] = True
                dp_y_tmp[i-ai] = True
        dp_y = dp_y_tmp

if dp_x[n*10+x] and dp_y[n*10+y]:
    print('Yes')
else:
    print('No')
            

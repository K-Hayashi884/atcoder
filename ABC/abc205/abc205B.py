n = int(input())
a = list(map(int, input().split()))
flg = True
for i in range(1,n+1):
    if i not in a:
        flg = False

if flg:
    print('Yes')
else:
    print('No')
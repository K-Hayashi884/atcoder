import numpy as np
n = int(input())
a = list(map(int, input().split()))
ans = 0
arr = np.zeros(n)
arr[0] = 2
arr[1] = 3
for i in range(2,n):
    arr[i] = arr[i-1] + arr[i-2]

def fib(num):
    if num == 0 or num==-1:
        return 1
    else:
        return arr[num-1]

ans = a[0] * fib(n-1)
for i in range(1, n):
    plus = fib(i-1)*fib(n-i-1)
    minus = fib(i-2)*fib(n-i-2)
    ans += a[i] * (plus-minus)
print(int(ans%(10**9+7)))
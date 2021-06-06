n = int(input())
a = list(map(int, input().split()))
s = 0
m = 0
array = [0]
offset = [0]
for i in range(n): 
    m = a[i] if a[i] > m else m
    s += a[i]
    print(s + m*(i+1) + offset[i])
    array.append(array[i] + a[i])
    offset.append(offset[i] + array[i+1])

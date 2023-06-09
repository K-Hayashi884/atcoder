a, b, c = list(map(int, input().split()))
if a >= 0 and b >= 0:
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')
else:
    if c%2 == 0:
        if abs(a) > abs(b):
            print('>')
        elif abs(a) < abs(b):
            print('<')
        else:
            print('=')
    else:
        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('=')
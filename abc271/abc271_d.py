from re import A


n, s = list(map(int, input().split()))
dp_flg = [0]*10000
dp_cards = [""]*10000
a, b = list(map(int, input().split()))
dp_flg[a-1] = 1
dp_flg[b-1] = 1
dp_cards[a-1] = "H"
dp_cards[b-1] = "T"

for _ in range(n-1):
    a, b = list(map(int, input().split()))
    dp_flg_tmp = [0]*10000
    dp_cards_tmp = [""]*10000
    for i in range(10000):
        if dp_flg[i]:
            dp_flg_tmp[i+a] = 1
            dp_flg_tmp[i+b] = 1
            dp_cards_tmp[i+a] = dp_cards[i]+"H"
            dp_cards_tmp[i+b] = dp_cards[i]+"T"
    dp_flg = dp_flg_tmp
    dp_cards = dp_cards_tmp

if dp_flg[s-1]:
    print("Yes")
    print(dp_cards[s-1])
else:
    print("No")

s_list = []
for _ in range(9):
    s_list.append(input())

polls = []
for ar, s in enumerate(s_list):
    for ac in range(9):
        if s[ac] == "#":
            polls.append([ar,ac])

cnt = 0
for i in range(len(polls)):
    for j in range(i+1, len(polls)):
        mid = [(polls[i][0]+polls[j][0])/2, (polls[i][1]+polls[j][1])/2]
        res = [polls[i][0]-mid[0], polls[i][1]-mid[1]]
        if [mid[0]-res[1], mid[1]+res[0]] in polls and [mid[0]+res[1], mid[1]-res[0]] in polls:
            cnt += 1

print(int(cnt/2))
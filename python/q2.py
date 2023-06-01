
def celebridade(G):
    m = -1
    for i in range(len(G)):
        if i<=m:
            continue
        flag = 1
        c=0
        while True:
            if c==len(G):
                break
            if c == i:
                c+=1
                continue
            if G[c][i]==0:
                flag =0
                m=c-1
                break
            c+=1
        if flag == 1:
            for w in range(len(G)):
                if G[i][w] == 1:
                    flag = 0
                if flag == 0:
                    return False
            if flag == 1:
                return True
    return False

x = [[0,1,1],[1,0,1],[0,0,0]]

print(celebridade(x))
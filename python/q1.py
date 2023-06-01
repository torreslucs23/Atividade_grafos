

def transposta_matriz(G):
    colunas = len(G)
    transposta=[]
    for i in range(colunas):
        linha = []
        for w in G:
            linha.append(w[i])
        transposta.append(linha)
    return transposta

def transposta_adjacencia(G):
    transposta ={i:[] for i in G}
    
    for i in G:
        for w in G[i]:
            transposta[w].append(i)
    return transposta


x = {"a":["b"], "b":["d"],"c":[],"d":["c","a"]}

y = [[0,1,0,0],[0,0,0,1],[0,0,0,0],[1,0,1,0]]

print(transposta_matriz(y))
print(transposta_adjacencia(x))
    
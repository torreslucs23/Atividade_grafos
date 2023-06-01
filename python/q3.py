
def subgrafo(G, v):
    new_G = {i:[] for i in G}
    for i in G:
        if i == v:
            continue
        else:
            for w in G[i]:
                if w != i:
                    new_G[i].append(w)
    del[new_G[v]]
    return new_G

x = {"a":["b"], "b":["d"],"c":[],"d":["c","a"]}

def subgrafo(G, v):
    new_v = [i for i in G if i not in v]
    
    for j in new_v:
        new_G = {i:[] for i in G}
        for i in G:
            if i == j:
                continue
            else:
                for w in G[i]:
                    if w != j:
                        new_G[i].append(w)
        del[new_G[j]]
        G = new_G.copy()
    return new_G

x = {"a":["b","c"], "b":["a","c","d"],"c":["a","b","d"],"d":["b", "c"]}



#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Kruskal Algorithm -------
"""
steps To write :-
1.Sort all edges in Non-Decreasing order of Weight.
2.pick the smallest Edge.
  check if adding the edge forms cycle.
  if cycle is not formed _Include Edge else _Exclude Edge ---- HE is Me Deepak ;)
3.REpeat step 2 unless (V-1) edges are included.

"""

def find(parent,u):
    if parent[u] == -1:
        return u
    return parent[u] = find(parent,parent[u])

def union_op(src,dst,parent,rank):
    fromP = find(parent,src)
    toP = find(parent,dst)

    if rank[fromP] > rank[toP]:
        parent[toP] = fromP
    elif rank[fromP] < rank[toP]:
        parent[fromP] = toP
    else:
        parent[fromP] = toP
        rank[toP] += 1


def KruskalAlgo(graph,V,E):
    mst = []
    graph.sort(key = lambda x:x[2])
    parent = [-1 for _ in range(v)]
    rank = [0 for _ in range(v)]
    i = 0
    j = 0 
    while(i<V-1 and j < E):
        src = find(parent,graph[j][0])
        dst = find(parent,graph[j][1])
        if src == dst:
            j += 1
        continue
        union_op(src,dst)
        mst.append(graph[j])
        i += 1
    return mst 

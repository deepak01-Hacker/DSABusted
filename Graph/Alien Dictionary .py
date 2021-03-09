
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

def makeGraph(dictionary,K):
    graph = [[] for _ in range(K)]
    for i in range(len(dictionary)-1):
        word1 = dictionary[i]
        word2 = dictionary[i+1]
        for j in range(0,min(len(word1),len(word2))):
            if word1[j] != word2[j]:
                graph[ord(word1[j])-ord('a')].append(ord(word2[j])-ord('a'))
                break
    return graph

def topolicalSortUtil(graph,visited,u,result):
    visited[u] = True
    for v in graph[u]:
        if visited[v] == False:
            topolicalSortUtil(graph,visited,v,result)
    result.append(u)
    


def topolicalSort(graph):
    result = []
    visited = [False for _ in range(len(graph))]

    for u in range(len(graph)):
        if visited[u] == False :
            topolicalSortUtil(graph,visited,u,result)
    return result[::-1]



def aleinDictionary(dictionary,N,K):
    graph = makeGraph(dictionary,K)
    print(graph)
    result = topolicalSort(graph)
    ans = "abcdefghijklmnopqrstuvwxyz"
    for i in range(K):
        print(ans[result[i]],end=" ")
    print()


if __name__ == "__main__":
    N = 5 
    K = 4
    dictionary = ["baa","abcd","abca","cab","cad"]
    print(aleinDictionary(dictionary,N,K))

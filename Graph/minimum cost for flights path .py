
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ minimum Distance using K stops


class Solution(object):
    def findCheapestPrice5(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
            Bellman-Ford
        """
        dp = [float('inf') for _ in range(n)]
        dp[src] = 0
        for _ in range(K + 1):
            dpTmp = dp[:]  # copy by value
            for u, v, cost in flights:
                dpTmp[v] = min(dpTmp[v], dp[u] + cost)  # relax
            dp = dpTmp

        return dp[dst] if dp[dst] != float('inf') else -1

#----------------------------------------- BFS ======================

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append(flight[1:])

        q = []
        for nei in graph[src]:
            q.append(nei)

        cache = {}
        cheapest = -1
        for i in range(K + 1):
            size = len(q)
            for _ in range(size):
                v, cost = q.pop(0)
                if v == dst:
                    cheapest = cost if cheapest == -1 else min(cheapest, cost)
                else:
                    for nei in graph[v]:
                        if nei[1] + cost >= cheapest != -1:
                            continue
                        q.append([nei[0], nei[1] + cost])

        return cheapest


#---------------------------- Dijikstra;s
def findCheapestPrice6(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    """
        Dijkstra
    """
    graph = defaultdict(list)
    for flight in flights:
        graph[flight[0]].append((flight[2], 0, flight[1]))

    minHeap = [nei for nei in graph[src]]
    heapq.heapify(minHeap)

    while len(minHeap) > 0:
        cost, numOfStop, stop = heapq.heappop(minHeap)
        if stop == dst:
            return cost
        elif numOfStop < K:
            for nei in graph[stop]:
                heapq.heappush(minHeap, (cost + nei[0], numOfStop + 1, nei[2]))

    return -1


 #-------------------- this Code from Deepak's universe ------------- \/ ---
if __name__ == "__main__":
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    s = Solution()
    n = 3
    src = 0
    dst = 2
    k = 1
    print(s.findCheapestPrice(n,flights,src,dst,k))

 




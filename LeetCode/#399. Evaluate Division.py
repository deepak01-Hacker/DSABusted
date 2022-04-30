
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = collections.defaultdict(lambda: collections.defaultdict(int))
        vset = set()
        for e, v in zip(equations, values):
            g[e[0]][e[1]] = v
            g[e[1]][e[0]] = 1.0 / v
            vset.add(e[0])
            vset.add(e[1])
        for k in vset:
            g[k][k] = 1.0
            for s in vset:
                for t in vset:
                    if g[s][k] and g[k][t]:
                        g[s][t] = g[s][k] * g[k][t]
        ans = []
        for s, t in queries:
            ans.append(g[s][t] if g[s][t] else -1.0)
        return ans
        

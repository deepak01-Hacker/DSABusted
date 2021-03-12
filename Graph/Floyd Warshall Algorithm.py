#fun fact is that !

#@ Floyd Warshall ===== :)
#Taste of DP


class Solution:
    def shortest_distance(self, matrix):
        dist = [[ matrix[i][j] if matrix[i][j] != -1 else 9999999999 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        v = len(matrix)
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
        for i in range(v):
            for j in range(v):
                if dist[i][j] == 9999999999:
                    dist[i][j] = -1
        return dist



if __name__ == "__main__":
    matrix = [[0,25],
             [-1,0]]
    s1 = Solution()
    print(s1.shortest_distance(matrix))

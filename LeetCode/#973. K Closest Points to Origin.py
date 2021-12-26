import math,heapq
class Solution(object):
    def calculate(self,xi,yi):
		xi *= xi
		yi *= yi

		return math.sqrt(xi+yi)
    def kClosest(self, points, k):
		q = []        

		heapq.heapify(q)

		for i in range(len(points)):
			dist = self.calculate(points[i][0],points[i][1])

			heapq.heappush(q,[-dist,i])

			#print(q)

			if len(q) > k:
				heapq.heappop(q)

		for i in range(len(q)):
			index = q[i][1]
			q[i][0] = points[index][0]
			q[i][1] = points[index][1]
		return q
			


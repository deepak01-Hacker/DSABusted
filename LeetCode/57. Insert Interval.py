class Solution(object):
    def insert(self,intervals,newInterval):
        n = len(intervals)
        
        if n == 0:
            return [newInterval]
        
        insertHappen = False
    
        for i in range(0,n):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i,newInterval)
                insertHappen = True
                break

        if insertHappen == False and i == n-1:
            intervals.append(newInterval)
        else:
            i -= 1 if i > 0 else 0

        while(i < n):
            #print(intervals[i])
            if intervals[i][1] >= intervals[i+1][0] :
                if intervals[i+1][1] > intervals[i][1]:
                    intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
                n -= 1

            else:
                i += 1
        return intervals



class Solution(object):
    def carPooling(self, trips, capacity):
        
        map = {}
        
        for i in range(len(trips)):
            num = trips[i][0]
            start = trips[i][1]
            end = trips[i][2]
            
            if start not in map:
                map[start] = 0
                
            if end not in map:
                map[end] = 0
                
            map[start] += num
            map[end] -= num
            
        currPass = 0
        print(map)
        
        for k in sorted(map.keys()):
            passengers = map[k]
            
            currPass += passengers
            if currPass > capacity:
                return False
        return True

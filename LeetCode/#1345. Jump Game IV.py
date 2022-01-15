class Solution(object):
    def minJumps(self, arr):
        
        q = []
        
        map = {}
        
        for i in range(len(arr)):
            
            try:
                map[arr[i]].append(i)
            except:
                map[arr[i]] = [i]
                
            
        q.append([0,1])
                
        while(q):
            #print(map)

            index,count = q.pop(0)
            #print(index,count)
            
            if index == len(arr)-1:
                return count-1
            #print(index)
            
            if arr[index] in map:
                for newIndex in map[arr[index]]:
                    if index != newIndex:
                        q.append([newIndex,count+1])

                del map[arr[index]]

            if index-1 >= 0 and arr[index-1] in map:
                q.append([index-1,count+1])

            if index+1 < len(arr) and arr[index+1] in map :
                q.append([index+1,count+1])
            
        return count
        #[7,7,2,1,7,7,7,3,4,1]
        

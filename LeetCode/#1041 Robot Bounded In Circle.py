dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution(object):
    def isRobotBounded(self, instructions):
        x = 0
        y = 0
        
        i = 0
        for _ in range(4):
            for cmd in instructions:
                if cmd == "G":
                    dx, dy = dirs[i]
                    x += dx
                    y += dy
                elif cmd == "L":
                    i = (i - 1) % 4
                else:
                    i = (i + 1) % 4
                    
        return x == 0 and y == 0
        
        
        
        

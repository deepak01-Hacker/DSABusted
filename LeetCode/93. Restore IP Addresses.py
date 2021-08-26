anss = [] #temprory validations

class Solution(object):
    def validSlot(self,ip):
        if ip and int(ip) >= 0 and int(ip) <= 255 and abs(len(ip)-len(str(int(ip)))) == 0:
            return True

    def utils(self,ip,res):

        if len(anss) > 4:
            return False

        #print(ip)
        for i in range(1,len(ip)):
            
            if self.validSlot(ip[:i]):
                anss.append(ip[:i])
                
                if self.validSlot(ip[i:]):
                    anss.append(ip[i:])
                    
                    if len(anss) == 4:
                        res.append(tuple(anss))
                        
                    anss.pop()
                    
                self.utils(ip[i:],res)
                anss.pop()
                
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        try:
            number = int(s)
        except:
            return []
        
        res = [] # result array
        
        self.utils(s,res)
        for i in range(len(res)):
            res[i] = '.'.join(res[i])
        
        return res

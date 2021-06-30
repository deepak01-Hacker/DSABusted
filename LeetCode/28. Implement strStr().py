class Solution(object):
    
    def prefixPattern(self,haystack,lps,M):
        len_ = 0
        i = 1
        
        while(i < M):
            if haystack[i] == haystack[len_]:
                len_ += 1
                lps[i] = len_
                i += 1
            else:
                
                if len_ != 0:
                    len_ = lps[len_-1]
                else:
                    lps[i] = 0
                    i += 1
            
    
    def strStr(self, haystack, needle):
        
        if needle == "" and haystack == "":
            return 0
        elif (needle and haystack==""):
            return -1
        elif (needle == "" and haystack):
            return 0
        
        #KMP ALgo
        
        M = len(haystack)
        N = len(needle)
        
        lps = [0]*N
        
        self.prefixPattern(needle,lps,N)
        

        #print(lps)
        i = 0  #haystack
        j = 0  #needle
        
        while(i < M):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                
            if j == N:

                return (i-N)
            
            elif i < M and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j-1]
                    
                else:
                    i += 1
                
        return -1
        
        

class Solution(object):
    def isPalindrome(self, s):
        if s == "":
            return True

        i = 0
        j = len(s)-1

        while(i<=j):

            if s[i].isalnum() and s[j].isalnum():  # isalnum() ---> prefdefined function for checling string belongs to alphabet and numeric.
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            else:
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1
        return True

        

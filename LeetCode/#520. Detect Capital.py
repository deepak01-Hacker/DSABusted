class Solution(object):
    def detectCapitalUse(self, word):
        current = word
        
        if word.lower() == current or word.upper() == current:
            return True
        
        st = word[0]
        st = st.upper()
        
        if len(word) > 1:
            temp = word[1:]
            temp = temp.lower()
            st += temp
            
        
        
        if st == current:
            return True
        return False
        

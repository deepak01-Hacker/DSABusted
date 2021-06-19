class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringOfNum = str(x)
        return stringOfNum  == stringOfNum[::-1]

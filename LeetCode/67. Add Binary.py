class Solution(object):
    def addBinary(self, b1, b2):
        ans = ""
        carry = 0

        a = len(b1)-1
        b = len(b2)-1

        while(a >=0 and b>=0):
            x = int(b1[a])+carry if int(b1[a])+carry < 2 else 0


            carry = 1 if int(b1[a])+carry == 2 else 0


            if carry:
                x += int(b2[b])
                ans += str(x)

            else:
                x += int(b2[b])
                if x == 2:
                    carry = 1
                    ans += '0'
                elif x == 1:
                    carry = 0
                    ans += '1'
                else:
                    carry = 0
                    ans += '0'
            a -= 1
            b -= 1

        while(a >= 0):
            x = int(b1[a])+carry if int(b1[a])+carry < 2 else 0

            carry = 1 if int(b1[a])+carry == 2 else 0

            ans += str(x)

            a -= 1

        while(b >= 0):
            x = int(b2[b])+carry if int(b2[b])+carry < 2 else 0

            carry = 1 if int(b2[b])+carry == 2 else 0

            ans += str(x)

            b -= 1

        if carry:
            ans += '1'

        return ans[::-1]






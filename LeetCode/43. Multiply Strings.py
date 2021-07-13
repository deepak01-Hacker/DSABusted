class Solution(object):
    def multiply(self, st1, st2):
        ans = 0

        ct = 0
        for val in range(len(st1)-1,-1,-1):
            carry = 0
            mul = ""
            for op in reversed(st2):
                res = int(op)*int(st1[val])
                res += carry

                carry = res//10
                temp = str(res%10)
                temp += mul
                mul = temp
                #print(temp)

            if carry:
                temp = str(carry)
                temp += mul
                mul = temp
            #print(mul)
            ans += int(mul)*10**ct
            ct += 1
        return str(ans)


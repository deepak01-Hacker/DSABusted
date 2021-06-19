import sys

class Solution:
    def myAtoi(self, Str: str) -> int:
        if Str == " " or Str == "":
            return 0

        maxsize = (2**31)

        sign, base, i = 1, 0, 0

        while (i <len(Str) and Str[i] == " "):
            i += 1

        if i == len(Str):
            return 0

        if (Str[i] == "-" or Str[i] == "+"):
            sign = 1 - 2 * (Str[i] == "-")
            i += 1

        while (i < len(Str) and
                Str[i] >= "0" and Str[i] <= "9"):

            if (base > (maxsize-1 // 10) or
                (base == (maxsize-1 // 10) and
                (Str[i] - "0") > 7)):
                if (sign == 1):
                    return maxsize-1
                else:
                    return -(maxsize)

            base = 10 * base + (ord(Str[i]) - ord("0"))
            i += 1

        intResult = base * sign
        if intResult <= -2**31:
            return -2**31
        elif intResult >= (2**31)-1:
            return (2**31)-1
        else:
            #print('Y')
            return intResult


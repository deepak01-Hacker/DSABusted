
def Divide(div,divisor):

    ans = 0

    if div < divisor:
        return ans

    cnt = 0
    while(div-divisor >= 0):
        cnt += 1
        ans = cnt
        div -= divisor

    return ans

def bitDivide(div,divisor):

    if div < divisor:
        return 0

    sig = -1 if div < 0 or divisor < 0 else 1

    div = abs(div)

    divisor = abs(divisor)

    q = 0
    temp = 0

    for i in range(31,-1,-1):
        if (temp+(divisor) << i) <= dividend:
            temp += divisor << i
            q |= 1 << i
            print(q,divisor<<i,1<<i,q)

    return q*sig





if __name__ == "__main__":
    dividend = 10
    divisor = 3

    print(bitDivide(dividend,divisor))




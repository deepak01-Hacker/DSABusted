
def nextPermutation(num):

    for i in range(len(num)-1,0,-1):
        if num[i] > num[i-1]:
            break

    if num[i-1] > num[i]:
        i -= 1
    
    if i != 0:
        for j in range(len(num)-1,i-1,-1):
            if (num[i-1] < num[j]):
                num[i-1],num[j] = num[j],num[i-1]
                break

    num = num[:i]+sorted(num[i:])
    return num


if __name__ == "__main__":
    s = [1,1,5]
    print(nextPermutation(s))

#pyhon3


#Without modification # Floyd's Tortoise and hare

def findDuplicates(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1

if __name__ == "__main__":
    print(findDuplicates([3,1,3,4,2]))

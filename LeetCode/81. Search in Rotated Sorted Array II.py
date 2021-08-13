class Solution(object):

    def search(self, arr, target):
        left = 0
        right = len(arr)-1

        while(left<=right):

            mid = left + (right-left)//2

            if arr[mid] == target:
                return True

            if arr[mid] == arr[left]:
                left += 1
                continue

            if (arr[left] <= target) ^ (arr[left] <= arr[mid] ):

                if (arr[left] <= arr[mid]):

                    left = mid+1

                else:
                    right = mid-1
            else:
                if (arr[mid] < target):
                    left = mid+1
                else:
                    right = mid-1

        return False

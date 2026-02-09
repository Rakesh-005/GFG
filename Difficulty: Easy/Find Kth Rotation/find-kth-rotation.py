class Solution :
    def findKRotation(self, arr):
        cnt = 0

        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                cnt = i
                break
        return cnt
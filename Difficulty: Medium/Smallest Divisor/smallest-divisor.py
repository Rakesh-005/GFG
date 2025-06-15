import math

class Solution:
    def smallestDivisor(self, arr, k):
        def is_possible(divisor):
            return sum(math.ceil(num / divisor) for num in arr) <= k
        
        low = 1
        high = max(arr)
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return answer

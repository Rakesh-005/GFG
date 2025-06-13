#User function Template for python3
from math import ceil
class Solution:
    def kokoEat(self,piles,h):
        # Code here
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            hours_required = sum(ceil(pile / mid) for pile in piles)
            if hours_required > h:
                low = mid + 1
            else:
                high = mid
        return low
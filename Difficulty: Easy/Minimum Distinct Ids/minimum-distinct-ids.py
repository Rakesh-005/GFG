#User function Template for python3

from collections import Counter
class Solution:
    def distinctIds(self,arr : list, n : int, m : int):
        count = Counter(arr)
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        while count and count[-1][1] <= m:
            m -= count.pop()[1]
        return len(count)
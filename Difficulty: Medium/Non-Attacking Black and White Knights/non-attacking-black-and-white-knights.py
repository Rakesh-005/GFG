class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        total=m*n
        ans=total*(total-1)
        cap=0
        if n>=2 and m>=3:
            cap+=4*(m-2)*(n-1)
        if n>=3 and m>=2:
            cap+=4*(n-2)*(m-1)
        return ans-cap
class Solution:
    def rearrange(self, arr, x):
        arr.sort(key=lambda i:abs(i-x))
        return arr
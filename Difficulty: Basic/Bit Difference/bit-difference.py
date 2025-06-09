class Solution:
    def countBitsFlip(self, a, b):
        #code here
        return bin(a^b).count('1')
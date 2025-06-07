class Solution:
    def minFlips(self, S):
        # Case 1: starting with '0'
        flip0 = 0
        expected = '0'
        for c in S:
            if c != expected:
                flip0 += 1
            # Alternate expected bit
            expected = '1' if expected == '0' else '0'
        
        # Case 2: starting with '1'
        flip1 = 0
        expected = '1'
        for c in S:
            if c != expected:
                flip1 += 1
            expected = '1' if expected == '0' else '0'
        
        # Return minimum flips
        return min(flip0, flip1)

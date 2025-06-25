from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = Counter(s)
        vals = list(freq.values())
        count_freq = Counter(vals)
        
        if len(count_freq) == 1:
            # All characters already have the same frequency
            return True
        elif len(count_freq) == 2:
            key1, key2 = count_freq.keys()
            val1, val2 = count_freq[key1], count_freq[key2]
            
            # Case 1: One character occurs once and has frequency 1 (e.g., {1:1, 3:4})
            if (key1 == 1 and val1 == 1) or (key2 == 1 and val2 == 1):
                return True
            
            # Case 2: The difference between frequencies is 1 and the higher one occurs once
            if abs(key1 - key2) == 1:
                if (count_freq[key1] == 1 and key1 > key2) or (count_freq[key2] == 1 and key2 > key1):
                    return True
        
        return False

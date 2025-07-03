class Solution:
    def longestKSubstr(self, s, k):
        # code here
        n = len(s)
        left = 0
        max_len = -1
        char_map = {}
    
        for right in range(n):
            # Add current character to the map
            char_map[s[right]] = char_map.get(s[right], 0) + 1
    
            # Shrink window if distinct characters > k
            while len(char_map) > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1
    
            # Check if window has exactly k distinct characters
            if len(char_map) == k:
                max_len = max(max_len, right - left + 1)
    
        return max_len
        
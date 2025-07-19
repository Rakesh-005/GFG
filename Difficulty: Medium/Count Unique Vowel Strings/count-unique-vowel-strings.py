class Solution:
    def vowelCount(self, s):
        vowels = 'aeiou'
        count = {}
    
        # Count occurrences of each vowel in the string
        for ch in s:
            if ch in vowels:
                if ch in count:
                    count[ch] += 1
                else:
                    count[ch] = 1
    
        # If no vowels found
        if not count:
            return 0
    
        # Calculate product of choices (pick 1 occurrence for each vowel)
        product = 1
        for v in count:
            product *= count[v]
    
        # Calculate factorial of number of distinct vowels
        n = len(count)
        fact = 1
        for i in range(2, n + 1):
            fact *= i
    
        return product * fact

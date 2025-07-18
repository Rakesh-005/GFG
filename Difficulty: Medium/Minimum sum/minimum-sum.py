#User function Template for python3
def addNumbers(l1, l2):
        i = len(l1) - 1
        j = len(l2) - 1
    
        # initial carry is zero
        carry = 0
    
        # we will calculate and store the 
        # resultant sum in reverse order in res
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            if i >= 0:
                total += l1[i]
            
            if j >= 0:
                total += l2[j]
            
            res.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
    
        # remove leading zeroes which are currently
        # at the back due to reversed string res
        while len(res) > 0 and res[-1] == '0':
            res.pop()
    
        # reverse our final result
        res = res[::-1]
        return ''.join(res)
class Solution:
    
    # Function to find and return minimum sum of
    # two numbers formed from digits of the array.
    def minSum(self,arr):
        arr.sort()
    
        # Two Lists for storing the two minimum numbers
        l1 = []
        l2 = []
    
        for i in range(len(arr)):
            if i % 2 == 0:
                l1.append(arr[i])
            else:
                l2.append(arr[i])
    
        return addNumbers(l1, l2)



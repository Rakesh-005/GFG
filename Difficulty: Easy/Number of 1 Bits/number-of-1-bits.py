#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		return bin(n)[2:].count('1')
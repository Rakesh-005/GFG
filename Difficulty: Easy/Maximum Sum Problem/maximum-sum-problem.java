// User function Template for Java

class Solution {
       int dp(int n){
            if(n<12) return n;
            int sum = dp(n/2) + dp(n/3) + dp(n/4);
            
            return sum;
        }
        int maxSum(int n)
        {
            //code here.
            if(n<12) return n;

            return dp(n);
        }
}

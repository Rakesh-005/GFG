// User function Template for Java
class Solution {
    public static int[] productExceptSelf(int arr[]) {
        // code here
        int n = arr.length;
        int lPrefix[] = new int[n];
        
        // left prefix product
        lPrefix[0] = 1;
        for(int i=1;i<n;i++)
        {
            lPrefix[i] = lPrefix[i-1] * arr[i-1]; 
        }
        
        int prod = 1;
        for(int i = n-1;i>=0;i--)
        {
            lPrefix[i] = prod * lPrefix[i];
            prod = prod * arr[i];
        }
        
        return lPrefix;
    }
}

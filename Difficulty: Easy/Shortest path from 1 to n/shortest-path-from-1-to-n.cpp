// User function Template for C++

class Solution {
    
public:
    int minimumStep(int n){
        if(n<=1) return 0;
        if(n==2) return 1;
        int rem = n % 3;
        int res = rem + minimumStep(n/3) + 1;
        return res;
    }
};
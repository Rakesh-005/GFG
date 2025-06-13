// User function Template for C++

class Solution {
  public:
     void getMaxPathSum(Node* root,int &maxSum,int sum){
        if(root ==NULL)return;
        if(root->left==NULL && root->right==NULL)
       maxSum = max(maxSum,sum+root->data);
        getMaxPathSum(root->left,maxSum,sum+root->data);
        getMaxPathSum(root->right,maxSum,sum+root->data);
        
        
    }
    int maxPathSum(Node* root)
    {
        int maxSum=INT_MIN;
        int sum =0;
        getMaxPathSum(root,maxSum,sum);
        
        return maxSum;
    }
};
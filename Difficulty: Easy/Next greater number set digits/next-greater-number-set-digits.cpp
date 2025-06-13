
class Solution {
  public:
    int findNext(int N) {
        // code here.
        string s = to_string(N);
bool b = next_permutation(s.begin(),s.end());
if(!b) return -1;
return stoi(s);
    }
};
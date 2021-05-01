



#include <bits/stdc++.h>
using namespace std;


#define mod 1000000007
class Solution {
  public:
    long long int countBT(int h) { 
        long long int dp[h+1];
        dp[0] = dp[1] = 1;
        for(int i=2;i<=h;i++){
            dp[i] = (dp[i - 1] * ((2 * dp [i - 2])%mod + dp[i - 1])%mod) % mod;
        }
        return dp[h];
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int h;
        cin >> h;
        Solution ob;
        cout<<ob.countBT(h)<<endl;  
    }
    return 0;
}
  // } Driver Code Ends

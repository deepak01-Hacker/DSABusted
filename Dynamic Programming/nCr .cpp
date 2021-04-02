// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++
#define mod 1000000007

class Solution{
public:
    int nCr(int n, int r) {
        if (r > n)
            return 0;
        if (r > n - r)
            r = n - r;
        int dp[r + 1] = {0};
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = min(i, r); j >= 0; j--)
                dp[j] = (dp[j - 1] % mod + dp[j] % mod) % mod;
            }
        return dp[r] % mod;
        }
};

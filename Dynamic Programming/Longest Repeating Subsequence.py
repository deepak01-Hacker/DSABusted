

#----------------- GFG problem solved -------------------


#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
	public:
		int LongestRepeatingSubsequence(string str){
		    int len = str.size();
		    int dp[len+1][len+1];
		    for(int i = 0 ;i<=len;++i){
		        for (int j=0;j<=len;++j){
		            if ((i == 0) || (j == 0)){
		                dp[i][j] = 0;   
		            }
		            else if ((i != j ) && (str[i-1] == str[j-1])){
		                dp[i][j] = dp[i-1][j-1] + 1;
		            }
		            else{
		                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
		            }
		        }
		    }
		    return dp[len][len];
		    
		}

};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string str;
		cin >> str;
		Solution obj;
		int ans = obj.LongestRepeatingSubsequence(str);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends

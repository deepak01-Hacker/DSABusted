#Practice link :- 


#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
		

	public:
	int maxSumIS(int arr[], int n)  
	{  
	    int dp[n];
	    for(int k=0;k<n;k++){
	        dp[k] = arr[k];
	    }
	    for(int i=0;i<n;i++){
	        for(int j=i+1;j<n;j++){
	            if ((arr[i] < arr[j]) && (dp[j] < dp[i]+arr[j])){
	                dp[j] = dp[i]+arr[j];
	            }
	        }
	    }
	    return *max_element(dp,dp+n);
	    
	}  
};

// { Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        int a[n];

        for(int i = 0; i < n; i++)
        	cin >> a[i];

      

	    Solution ob;
	    cout << ob.maxSumIS(a, n) << "\n";
	     
    }
    return 0;
}

  // } Driver Code Ends

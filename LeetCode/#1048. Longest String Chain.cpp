class Solution {
public:
    int longestStrChain(vector<string>& words) {
        /// dp[i] = longest chain of words till i-th index
        sort(words.begin(), words.end(), [](string a, string b){
            return a.size() < b.size();
        }); /// why sort?, because, we want to solve it for smaller subproblems first
        unordered_map<string, int> dict;
        for(int i=0;i<words.size();i++)
                dict[words[i]] = i;
        vector<int> dp(words.size(), 1);
        int max_ = 0;
        for(int j=0;j<words.size();j++){
            string word = words[j];
            for(int k=0;k<word.size();k++){
                string nword = word.substr(0, k) + word.substr(k+1);
                if(dict.count(nword)){
                    int z = dict[nword];
                    if(dp[j] < 1 + dp[z]){
                        dp[j] = 1 + dp[z];
                    }
                }
            }
            max_ = max(max_, dp[j]);
        }
        return max_;
    }
};

class Solution {
public:
    int counter=0;
    unordered_map<string,string> dict;

    string encode(string longUrl) {
        char cmap[] = "abcdefghijklmnopqrstuvwxyz\
            ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        int n = (++counter);
        string shortUrl;
        while(n){
            shortUrl.push_back(cmap[n%62]);
            n=n/62;
        }
        reverse(shortUrl.begin(), shortUrl.end());
        dict[shortUrl] = longUrl;
        return shortUrl;
    }

    string decode(string shortUrl) {
        return dict[shortUrl];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));

class Solution {
public:
    bool checkPalindrome(string str)
    {
        int len = str.length();
        len--;
        for (int i=0; i<len; i++)
        {
            if (str[i] != str[len])
                return false;
            len--;
        }
        return true;
    }
    void addStrings(vector<vector<string> > &v, string &s,
                vector<string> &temp, int index)
    {
        int len = s.length();
        string str;
        vector<string> current = temp;
        if (index == 0)
            temp.clear();
        for (int i = index; i < len; ++i)
        {
            str = str + s[i];
            if (checkPalindrome(str))
            {
                temp.push_back(str);
                if (i+1 < len)
                    addStrings(v,s,temp,i+1);
                else
                    v.push_back(temp);
                temp = current;
            }
        }
        return;
    }
    vector<vector<string>> partition(string s) {
        vector<vector<string>> v;
        vector<string> temp;
        addStrings(v, s, temp, 0);
        return v;
        
    }
};

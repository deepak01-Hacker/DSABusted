class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        int element;
        
        map<int,int> set;       
        for (int i=0;i<nums.size();i++){
            element = nums[i];
            auto itr = set.find(target-element);
            if (itr != set.end()){
                result.push_back(itr->second);
                result.push_back(i);
                return result;
            }
            set.insert({nums[i],i});
        
        }
        return result;
    }
};

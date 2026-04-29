class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    
    {
        unordered_map<int, int> seen;

        for(int i = 0; i< nums.size(); i++)
        {
            //target - index search if true if any value in hash is equal to it
            int truth = target - nums[i];

            if(seen.count(truth))
            {
                return {seen[truth], i};
            }

            seen[nums[i]] = i;


        }
        return {};
        
    }
};

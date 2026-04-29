class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
        unordered_map<string, vector<string>> hash;

        for(int i =0; i< strs.size(); i++)
        {
            string word = strs[i];
            sort(word.begin(), word.end());

            hash[word].push_back(strs[i]);

        }
    vector<vector<string>> result;
    for (auto& [key, value] : hash) 
    {
        result.push_back(value);
    }

    return result;
    }
};
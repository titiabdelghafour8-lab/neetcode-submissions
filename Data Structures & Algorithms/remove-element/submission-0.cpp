class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        for (auto it = nums.begin(); it != nums.end();)
        {
            if (*it == val)
            {
                it = nums.erase(it);
            }
            else {
                count += 1;
                ++it;
            }
           
        }
        return count;
    }
};
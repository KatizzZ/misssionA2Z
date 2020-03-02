//Given an array of integers, return indices of the two numbers such that they a
//dd up to a specific target. 
//
// You may assume that each input would have exactly one solution, and you may n
//ot use the same element twice. 
//
// Example: 
//
// 
//Given nums = [2, 7, 11, 15], target = 9,
//
//Because nums[0] + nums[1] = 2 + 7 = 9,
//return [0, 1].
// 
// Related Topics Array Hash Table


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> m;
        for(int i=0; i<nums.size(); i++)
            m[nums[i]] = i;
        for(int i=0; i<nums.size(); i++){
            auto itr = m.find(target - nums[i]);
            if(itr!=m.end()){
                nums.clear();
                nums.push_back(i);
                nums.push_back(itr->second);
                return nums;
            }
        }
        nums.clear();
        return nums;
    }
};
//leetcode submit region end(Prohibit modification and deletion)

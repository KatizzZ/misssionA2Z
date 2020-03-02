//https://leetcode.com/problems/rectangle-overlap/
/* Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
*/
class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        return (rec1[2]>rec2[2] ? (rec1[0]<rec2[2] ? true: false) : (rec1[2]>rec2[0] ? true : false)) && (rec1[3]>rec2[3] ? (rec1[1]<rec2[3] ? true: false) : (rec1[3]>rec2[1] ? true : false));
    }
};
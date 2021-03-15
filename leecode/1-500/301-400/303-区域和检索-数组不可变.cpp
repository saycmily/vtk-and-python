class NumArray {
public:
    vector<int> num;
    NumArray(vector<int>& nums) {
        num = nums;
    }
    int sumRange(int i, int j) {
        int res = 0;
        for (int k = i; k < j+1; ++k)
            res += num[k];
        return res;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
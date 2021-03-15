class KthLargest {
public:
    vector<int> numbers;
    int z;
    KthLargest(int k, vector<int>& nums) {
        numbers = nums;
        sort(numbers.begin(), numbers.end());
        z = k;
    }
    int add(int val) {
        numbers.insert(upper_bound(numbers.begin(), numbers.end(), val), val);        
        return numbers[numbers.size()-z];
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
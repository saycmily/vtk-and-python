class Solution {
public:
    int reversePairs(vector<int>& nums) {
        int n = nums.size();
        vector<int> temp(n);
        int result = 0;
        mergesort(nums, temp, 0, n-1, result);
        return result;
    }
    void mergesort(vector<int>& nums, vector<int>& temp, int left, int right, int& result) {
        //只剩一个元素就是有序的了
        if (left >= right) return;
        //分隔点
        int mid = left + (right - left) / 2;
        //对左区间排序
        mergesort(nums, temp, left, mid, result);
        //对右区间排序
        mergesort(nums, temp, mid+1, right, result);
        int i = left, j = mid+1;
        //左右区间都是有序的了，进行统计操作
        while (i <= mid && j <= right) {
            if ((long long)nums[i] > (long long)2 * nums[j]) {
                //反转对个数
                result += mid - i + 1;
                j++;
            }
            else
                i++;
        }
        i = left; j = mid+1;
        int t = 0;
        //进行归并操作
        while (i <= mid && j <= right) {
            if (nums[i] > nums[j])
                temp[t++] = nums[j++];
            else
                temp[t++] = nums[i++];
        }
        //将左边剩余元素填充进temp中
        while (i <= mid)
            temp[t++] = nums[i++];
        //将右序列剩余元素填充进temp中
        while (j <= right)
            temp[t++] = nums[j++];
        t = 0;
        //将temp中的元素全部拷贝到原数组[left,right]中
        while (left <= right)
            nums[left++] = temp[t++] ;
    }
};
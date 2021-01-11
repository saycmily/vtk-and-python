#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int N = s.size();
        int UFS[N];

        // 初始化并查集数组
        for (int i = 0; i < N; ++i) {
            UFS[i] = i;
        }

        // 遍历边表, 并集连通, 每个结点值表示s中的下标
        for (auto& each : pairs) {
            unite(UFS, each[0], each[1]);
        }

        // 遍历并查集数组, 获取每个连通图
        // root, 邻接表
        unordered_map<int, vector<int>> graph;
        for (int i = 0; i < N; ++i) {
            int root = find(UFS, i);
            graph[root].push_back(i);
        }

        // 遍历每个连通图
        for (auto [root, arr] : graph) {
            radixSort(arr);
            string str;
            str.reserve(arr.size());

            // 收集表里每个下标到对应的字符道str中
            for (int idx : arr) {
                str += s[idx];
            }
            // 对str进行字典序排序
            bucketSort(str);

            // 将str在替换到原来位置
            int ptr = 0;
            for (int idx : arr) {
                s[idx] = str[ptr++];
            }
        }
        return s;
    }

    // 并查集：查找
    int find(int UFS[], int i) {
        return UFS[i] == i ? i : UFS[i] = find(UFS, UFS[i]);
    }

    // 并查集：并集
    void unite(int UFS[], int a, int b) {
        int roota = find(UFS, a);
        int rootb = find(UFS, b);
        
        UFS[rootb] = roota;
    }

    // 字符串计数排序
    void bucketSort(string& str) {
        int bucket[26] = {0};
        for (char c : str) {
            ++bucket[c-'a'];
        }

        int ptr = 0;
        for (int i = 0; i < 26; ++i) {
            int n = bucket[i];
            while (n--) {
                str[ptr++] = 'a' + i;
            }
        }
    }

    // 0-5位十进制数基数排序
    void radixSort(vector<int>& nums) {
        vector<vector<int>> bucket(10);

        for (int bit=10; bit <=100000; bit *= 10) {
            // 装桶
            for (int i=0; i < nums.size(); ++i) {
                int num = nums[i] % bit;
                num /= bit / 10;
                bucket[num].push_back(nums[i]);
            }
            // 收集
            int ptr = 0;
            for (auto &eachBit : bucket) {
                for (int num : eachBit) {
                    nums[ptr++] = num;
                }
            }
            // 清桶
            for (auto &eachBit : bucket) eachBit.clear();
        }
    }
};
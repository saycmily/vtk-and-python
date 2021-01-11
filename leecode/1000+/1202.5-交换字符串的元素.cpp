#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

struct unionfind {
    vector<int> f;
    unionfind(int size) {
        f.resize(size);
        for (int i = 0; i < size; ++i) {
            f[i] = i;
        }
    }
    int find(int x) {
        if (x == f[x]) return x;
        return f[x] = find(f[x]);
    }
    void merge(int a, int b) {
        int p = find(a), q = find(b);
        if (p != q) f[p] = q;
    }
};
class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int size = s.size();
        unionfind uf(size);
        for (auto& iter : pairs) {
            uf.merge(iter[0], iter[1]);
        }
        unordered_map<int, vector<char>> hash;
        for (int i = 0; i < size; ++i) {
            hash[uf.find(i)].push_back(s[i]);
        }
        for (auto& [key, value] : hash) {
            sort(value.begin(), value.end(), [](int a, int b) {
                return a > b;
            });
        }
        for (int i = 0; i < size; ++i) {
            int temp = uf.find(i);
            s[i] = hash[temp].back();
            hash[temp].pop_back();
        }
        return s;
    }
};
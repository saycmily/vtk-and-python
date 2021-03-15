class Solution {
public:
    bool isValidSerialization(string preorder) {
        int degree = 1;
        int n = preorder.length();
        for (int i = 0; i < n; ++i) {
            if (preorder[i] == ',') continue;
            if (degree == 0) return false;
            if (preorder[i] == '#')
                degree -= 1;
            else {
                i ++;
                while(i < n && preorder[i] != ',' && preorder[i] != '#')
                    i ++;
                degree += 1;
                i --;
            }
        }
        return degree == 0;
    }
};
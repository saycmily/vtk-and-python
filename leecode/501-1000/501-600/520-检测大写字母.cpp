class Solution {
public:
    bool detectCapitalUse(string word) {
        int n = word.length();
        if (word[0] >= 'a') {
            for (int i = 1; i < n; ++i)
                if (word[i] < 'a')
                    return false;
        }
        if (word[1] < 'a') {
            for (int i = 2; i < n; ++i)
                if (word[i] >= 'a')
                    return false;
        } else {
            for (int i = 2; i < n; ++i)
                if (word[i] < 'a')
                    return false;
        }
        return true;

    }
};
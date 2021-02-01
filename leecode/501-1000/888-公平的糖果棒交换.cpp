class Solution {
public:
    vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
        int suma = 0, sumb = 0;
        for (auto a : A)
            suma += a;
        for (auto b : B)
            sumb += b;
        if (suma > sumb) {
            int c = (suma - sumb) / 2;
            for (auto a : A) 
                for (auto b : B)
                    if (a - b == c)
                        return {a, b};
        } else if (suma < sumb) {
            int c = (sumb - suma) / 2;
            for (auto a : A)
                for (auto b : B)
                    if (b - a == c)
                        return {a, b};
        }
        return {};
    }
};
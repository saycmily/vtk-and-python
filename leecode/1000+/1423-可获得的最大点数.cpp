class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int ret = 0;
        int tmpRes = 0;
        for (int i = 0; i < k; i++)
            tmpRes = tmpRes + cardPoints[i];
        int l = k - 1, r = cardPoints.size() - 1;
        ret = tmpRes;
        while (l >= 0) {
            tmpRes = tmpRes - cardPoints[l] + cardPoints[r];
            l--;
            r--;
            ret = ret < tmpRes ? tmpRes : ret;
        }
        return ret;
    }
};
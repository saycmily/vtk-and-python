class Solution:
    def findBestValue(self, arr, target: int) -> int:
        arr.sort()
        cur_sum, cur_min, cur_max = 0, 0, 0
        x, y, res = 0, 0, 0
        n = len(arr)
        for i in range(n):
            num = cur_sum + (n-i)*arr[i]
            cur_sum += arr[i]
            if num == target:
                return arr[i]
            elif num < target:
                cur_min = i
                x = target - num
            else:
                cur_max = i
                y = num - target
                break
        ans = 0
        if x == 0:
            ans = target//n
            if abs(target-ans*n) < abs(target-(ans+1)*n):
                return ans
            else:
                return ans+1
        if y == 0:
            return arr[-1]
        if x > y:
            res = y
            ans = arr[cur_max]
        else:
            res = x
            ans = arr[cur_min]
        jichu = sum(arr[:cur_min+1])
        x = n - cur_min - 1
        for i in range(arr[cur_min]+1, arr[cur_max]):
            cur = abs(jichu + i*x - target)
            if cur < res:
                ans = i
                res = cur
        return ans

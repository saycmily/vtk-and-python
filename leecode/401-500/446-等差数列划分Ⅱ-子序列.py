class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        N = len(A)
        num = 0     # 总的等差序列的个数
        
        # 等差数列个数数组
        # 第 n 个元素最后的数为 A[n] 的等差数列的一个映射表
        #   映射表的每一个元素表示公差为key的等差数列的个数 （尾数为A[n]）
        # 注意： 此处的等差数列包含仅有两个元素的数列
        distList = [dict() for i in range(N)]
        
        for i in range(1, N):
            for j in range(i):
                delta = A[i] - A[j]
                
                # 考虑只包含 A[j], A[i]的数列
                if delta in distList[i]:
                    distList[i][delta] += 1  
                else:
                    distList[i][delta] = 1    
                if delta in distList[j]:
                    # A[i] 可以加到所有以A[j]结尾的公差为delta的数列后面
                    distList[i][delta] += distList[j][delta]
                    num += distList[j][delta]
       
        return num

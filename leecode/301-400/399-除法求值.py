class Solution:
    def calcEquation(self, equations, values, queries):
        zifu = dict()
        count = 0
        for i in equations:
            for j in i:
                if j not in zifu:
                    zifu[j] = count
                    count += 1

        graph = [[-1.0] * count for _ in range(count)]
        for i in range(count):
            graph[i][i] = 1.0
        
        for index,value in enumerate(equations):
            a = zifu[value[0]]
            b = zifu[value[1]]
            k = values[index]
            graph[a][b] = k
            graph[b][a] = 1/k
        for i in range(count):
            for j in range(count):
                for k in range(count):
                    if j == k or graph[j][k] != -1.0:
                        continue
                    if graph[j][i] != -1.0 and graph[i][k] != -1.0:
                        graph[j][k] = graph[j][i]*graph[i][k]
        ans = []
        for i in queries:
            if i[0] not in zifu or i[1] not in zifu:
                ans.append(-1.0)
            else:
                a = zifu[i[0]]
                b = zifu[i[1]]
                ans.append(graph[a][b])
        return ans


a = Solution()
b = a.calcEquation([["a","b"],["c","d"]],
[1.0,1.0],
[["a","c"],["b","d"],["b","a"],["d","c"]])
print(b)
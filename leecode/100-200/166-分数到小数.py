class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = 1 if numerator*denominator >= 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)

        head = numerator//denominator
        head = str(head) if flag > 0 else '-'+str(head)

        rest = numerator % denominator
        res = []
        rest_dic = {}  # 注意到余数只能取0(除尽了),1,2,....denominator-1这么多情况,
        # 用字典计算余数出现的最后一次位置，一旦发生了重复代表从余数上一次在字典中记录的位置开始发生了循环
        ind = 0
        while(rest != 0 and rest not in rest_dic):
            rest_dic[rest] = ind
            rest *= 10
            res.append(str(rest//denominator))
            rest = rest % denominator
            ind += 1

        if not res:
            return head
        if rest == 0:
            return head+'.'+''.join(res)
        else:
            return head+'.'+''.join(res[:rest_dic[rest]]) + \
                '('+''.join(res[rest_dic[rest]:])+')'

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        one = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        two_less_20 = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        ten = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one[num]
            elif num < 20:
                return two_less_20[num-10]
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten[tenner] + ' ' + one[rest] if rest else ten[tenner]

        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one[hundred] + ' Hundred ' + two(rest) 
            elif not hundred and rest: 
                return two(rest)
            elif hundred and not rest:
                return one[hundred] + ' Hundred'

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num:
            return 'Zero'

        result = ''
        if billion:
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result

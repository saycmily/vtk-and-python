def countCharacters(self, words, chars):
    a_dict = {}
    ans = 0
    for i in chars:
        if i not in a_dict:
            a_dict[i] = 1
            continue
        a_dict[i] += 1
    for word in words:
        clone = a_dict.copy()
        flag = True
        for letter in word:
            if letter not in clone:
                flag = False
            else:
                if clone[letter] <= 0:
                    flag = False
                clone[letter] -= 1
        if flag:
            ans += len(word)
    return ans

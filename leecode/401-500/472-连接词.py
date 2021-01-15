class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        def search(word, pre_dict):
            if len(word)==0:
                return True
            cur_dict = pre_dict
            for i,c in enumerate(word):
                cur_dict = cur_dict.get(c,None)
                if not cur_dict:
                    return False
                if '#' in cur_dict:
                    if search(word[i+1:], pre_dict):
                        return True
            return False

        def insert(word, cur_dict):
            for c in word:
                if c not in cur_dict:
                    cur_dict[c] = {}
                cur_dict = cur_dict[c]
            cur_dict['#'] ={}

        words.sort(key=lambda x: len(x))
        ret = []
        pre_dict = {}
        for word in words:
            if len(word)==0:
                continue
            if search(word, pre_dict):
                ret.append(word)
            else:
                insert(word, pre_dict)
        return ret
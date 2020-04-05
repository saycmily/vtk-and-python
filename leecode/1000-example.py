from operator import itemgetter
# a = [1, 3, 2]
# a = sorted(a)
# print(a)
key_value = {1: {7: 2}, 2: {7: 1}, 3: {7: 3}}
# key_value = [[1,2], [3,1], [2,3]]
print(sorted(key_value.items(), key=itemgetter(0)))

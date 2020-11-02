# import os
# SOCKET_USER_FOLDER_PATH = "D:\\heihei"
# path = "D:/szyjy/notebook/jupyter_notebook_config.py"
# # if not os.path.exists(path):
# #     os.mkdir(path)
# fp_old = open(path, 'r')
# lines = fp_old.readlines()
# print(lines[286])
# port = '9999'
# print(lines[-2].split(' ')[-1][:-1])

# lines[-2] = 'c.NotebookApp.port = ' + str(port) + '\n'
# lines[-1] = "c.NotebookApp.notebook_dir = '" + path + "'"
# with open(SOCKET_USER_FOLDER_PATH+'\\222.txt', 'w') as f:
#     new_config_str = ''.join(lines)
#     f.write(new_config_str)

# a,b,*rest = [1,2,3,4]
# print(a,b,rest)
# import re
# message = 'level: I'
# res = re.match(r'level:\s(\w)', message)
# if res:
#     print(res.group(1)=='I')
# import time
# timestr = "2020-9-29 17:30:30"
# tiemcamp = time.mktime(time.strptime(timestr, '%Y-%m-%d %H:%M:%S'))
# print(tiemcamp)
# from flask_wtf import Form
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# print(issubclass(C,A))
# class a():
#     cla = 'aaa'
#     def __init__(self):
#         self.dd = 'bbb'

# import time
# import datetime
# s = '20201010-072732-ca18'

# a = time.strptime(s[:15], '%Y%m%d-%H%M%S')
# print(str(datetime.datetime(*a[:6])))

# print(sorted("12133"))

# import matplotlib.pyplot as plt
# lw = 2
# plt.figure(figsize=(10,5))
# plt.plot([0,1], [1,0], color='darkorange',
#          lw=lw, label='ROC curve (area = %0.2f)' % 0.99) ###假正率为横坐标，真正率为纵坐标做曲线
# plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic example')
# plt.legend(loc="lower right")
# plt.show()
# print('123' > '124')
# def func():
#     with open('jupyter.py', 'r', encoding='utf-8') as f:
#         a = f.readline()
#         a = a.split(',')
#         if False:
#             return a
#     return a
# print(func())
lines = ["a","b","v"]
for i in lines:
    if i == "b":
        lines.remove(i)
        break
print(lines)

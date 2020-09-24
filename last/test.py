# import os
# SOCKET_USER_FOLDER_PATH = "D:\\heihei"
# path = SOCKET_USER_FOLDER_PATH + '\\cmily'
# # if not os.path.exists(path):
# #     os.mkdir(path)
# fp_old = open(SOCKET_USER_FOLDER_PATH+'\\111.txt', 'r')
# lines = fp_old.readlines()
# port = '9999'
# print(lines[-2].split(' ')[-1][:-1])

# lines[-2] = 'c.NotebookApp.port = ' + str(port) + '\n'
# lines[-1] = "c.NotebookApp.notebook_dir = '" + path + "'"
# with open(SOCKET_USER_FOLDER_PATH+'\\222.txt', 'w') as f:
#     new_config_str = ''.join(lines)
#     f.write(new_config_str)

a,b,*rest = [1,2,3,4]
print(a,b,rest)
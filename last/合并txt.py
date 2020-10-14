import os

path = "D:/szyjy/标注/machining" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
txts = []
ans = 0
for file in files: #遍历文件夹
    position = path + '/' + file #构造绝对路径，"\\"，其中一个'\'为转义符、
#     i, y = -7, 1
#     num = 0
#     while file[i].isdigit():
#         num = num + int(file[i])*y
#         y = y*10
#         i = i - 1
#     ans += num
# print(ans)
    with open(position, "r", encoding='utf-8') as f:    #打开文件
        data = f.read()   #读取文件
        print(data)
        txts.append(data)
with open(path+'\\sum.txt', "w", encoding='utf-8') as f:
    f.write(''.join(txts))

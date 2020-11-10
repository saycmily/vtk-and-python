# a = '远望智库：与智者同行，为创新加速专家库 | 人才库 | 企业库 | 项目库 | 投'
# if '远望智库' in a:
#     print("nmsl")
i = 0
error_word = ['智库', '代码', '健康', '网络安全', '信息安全','脚本',\
'病','内网','金融','5G', '经济', '算法','人工智能','诗','Google', \
'手机', 'python', 'Windows','HTTP','中国移动','习近平']
with open("D:/szyjy/标注/标注原始数据/res_6.txt", 'r', encoding='utf-8') as f:
    st = f.readline()
    with open("D:/szyjy/标注/军事文本资料/4.txt", 'w', encoding='utf-8-sig') as g:
        while st:
            flag = True
            for err in error_word:
                if err in st:
                    flag = False
                    break
            if flag:
                g.write(st)
            st = f.readline()
           

import random
import time

# 根据毫秒随机数字
def haimiao():
    t = time.time()
    a = int(round(t*1000))
    b = str(a)[-1]
    return int(b)

# 参加人员
Participants = [
    "曹", "翟", "赵", "段", "汪",
    "苏", "阿泰", "祖", "大吃货", "小学弟"
]

# 输入上一局的比赛分配
a = [
    "大吃货", "赵", "祖", "小学弟", "曹",
    "翟", "苏", "阿泰", "汪", "段"
]

# 判断新的随机比赛和上一场是否有人相同位置
def same(b):
    for i in range(10):
        if a[i] == b[i] or a[i] == b[5-i]:
            return True
    return False

# 随机打乱
random.shuffle(Participants)
while same(Participants):
    random.shuffle(Participants)
message = " \n-----------------------------------------------------------------\n\n"
message += "蓝色方: "
for i in Participants[:5]:
    message += i + "  "
message += "    红色方: "
for i in Participants[5:]:
    message += i + "  "
message += "\n\n-----------------------------------------------------------------\n"
print(message)
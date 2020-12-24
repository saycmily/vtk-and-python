# -*- coding: utf-8 -*-
import requests
import time
import csv
import pandas as pd

# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用Cookie，跳过登陆操作
headers = {
  "Cookie": "appmsglist_action_3945197879=card; LW_uid=o1z5T8G5s5X6H4A6k7B5p9c255; qb_guid=81be3203d0dd4734850d913cca90d966; tvfe_boss_uuid=f09841388dd109fc; LW_pid=98c374b8c66d7f40ed4decb30a33b977; pgv_pvid=4298615155; Q-H5-GUID=81be3203d0dd4734850d913cca90d966; o_cookie=1923643958; ptcz=a0382331828585071d51ee0ccdc1c40948677fad982cda63d58f94a6b0c5c7ec; ied_qq=o1923643958; uin_cookie=o1923643958; pgv_pvi=3934434304; pac_uid=1_1923643958; iip=0; qb_qua=; ue_uk=db11efcd091c93aa3de87a08ab988857; ue_skey=d7399097bdfcac1786a92637aad8efd4; LOLWebSet_AreaBindInfo_1923643958=%257B%2522areaid%2522%253A%252214%2522%252C%2522areaname%2522%253A%2522%25E9%25BB%2591%25E8%2589%25B2%25E7%258E%25AB%25E7%2591%25B0%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221923643958%2522%252C%2522rolename%2522%253A%2522Say%25E4%25B8%25B6Si%25E4%25B8%25A8Cmily%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1923643958%257C14%257C1923643958*%257C%257C%257C%257CSay%2525E4%2525B8%2525B6Si%2525E4%2525B8%2525A8Cmily*%257C%257C%257C1592324542%2522%252C%2522md5str%2522%253A%2522F99AE4E43D094F640110D9FE256A8342%2522%252C%2522roleareaid%2522%253A%252214%2522%252C%2522sPartition%2522%253A%252214%2522%257D; RK=Lr48O0otcb; NetType=; eas_sid=y1p5k8p35667S8q5b6P706e2R6; ue_ts=1553527082; ue_uid=eb72c39f74964ba2da4d047e966f93cf; LW_sid=m1M5g988d6j0U2E2u2m1R4d0w0; Qs_lvt_323937=1606217866; Qs_pv_323937=1588048746613849000; _ga=GA1.2.951491700.1606217866; pgv_info=ssid=s8561600382; ua_id=9JdS6KzZsuHZaE76AAAAAOc0CKJz4oqGXsfp2gezB8Y=; pgv_si=s6605922304; uuid=0785e67836c7223eb3af6e1891248242; cert=8Inzlkwb87H6vH96ttsNiXoL4SR0Uewt; sig=h018239f33d963bd0d66f24a1345228c3e8f75af847d82d9524e277986e343134cf338d0ce773695438; data_bizuin=3945197879; data_ticket=Snwe9KkiGzVbYSHIbRLXfZIjQjDWIJrgdW+kkYwUCCGbX/ISEjvdML3+GCFaFWuH; master_key=YpP7xqmgYV/pl5bdAieU/M4xV1BHI2ZJ1vSiT7+qwC0=; master_user=gh_0aa32b354ff4; master_sid=UGJnd09BRFFxS1Ztem0xeTg0cVZKT25fbkx5WG5qNkdxbm43eldOd3BWWlY2d1N2TFRQTk5NYjFlMkU5Ymk4Q2Y2ZXRqNUg5WTQ3VlcyMVFQZ1dGZVNXWUhyc3hmdmlqMm5nVEFBRm5RdUZvVjhwa0ppTVBvamdIT3hPaXhDV3o2NFBQRUdMNWNSdlNpSUJu; master_ticket=2153e493ca19423e8cc9913fd11336e9; bizuin=3945197879; slave_user=gh_0aa32b354ff4; slave_sid=cFdtNXZCblZaejlWWVpSVHlwcDNRY1hSOWFSWlB4MndEQXY1X1hXZUZJb3ZnRlBtMExKSmhnZkdYa0syT0x1aUY3cGt0Tmw2ZjdKUGlpOUxQVFRsckx1NXdWOHVVcjQ3WTl2NUY2ZWJtSWFBZzhSM0JWenFqdUxPaHJCV1FNZmRMbmFnc1I3S2dFVjdDdXBT",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
}

data = {
    "token": "1875884698",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MzU5Nzg1NDIxOQ==",
    "type": "9",
}


content_list = []
for i in range(12):
    data["begin"] = i*5
    time.sleep(3)
    # 使用get方法进行提交
    content_json = requests.get(url, headers=headers, params=data).json()
    # 返回了一个json，里面是每一页的数据
    for item in content_json["app_msg_list"]:    
    # 提取每页文章的标题及对应的url
        items = []
        items.append(item["title"])
        items.append(item["link"])
        content_list.append(items)
    print(i)
name=['title','link']
test=pd.DataFrame(columns=name,data=content_list)
test.to_csv("xingzhengzhifa.csv",mode='a',encoding='utf-8')
print("保存成功")

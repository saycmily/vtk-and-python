#4.找出美国确诊最多的10个州
df4 = spark.sql("select date,state,totalCases from eachStateInfo  order by totalCases desc limit 10")
df4.repartition(1).write.json("result4.json")

#4.画出美国确诊最多的10个州——>词云图
def drawChart_4(index):
    root = "/home/hadoop/result/result" + str(index) +"/part-00000.json"
    data = []
    with open(root, 'r') as f:
        while True:
            line = f.readline()
            if not line:                            # 到 EOF，返回空字符串，则终止循环
                break
            js = json.loads(line)
            row=(str(js['state']),int(js['totalCases']))
            data.append(row)
 
    c = (
    WordCloud()
    .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="美国各州确诊Top10"))
    .render("/home/hadoop/result/result4/result1.html")
    )
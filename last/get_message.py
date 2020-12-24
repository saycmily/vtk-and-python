import pandas as pd
import requests
from lxml import etree


class WeixinSpider_1:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
        }

    def get_url_list(self):
        file_path = "cmily.csv"
        df = pd.read_csv(file_path)
        title_list = df["title"].tolist()
        url_list = df["link"].tolist()
        return title_list, url_list

    def parse_url(self, url):  
        response = requests.get(url, headers=self.headers)
        return response.content.decode()


    def run(self):  
  		# 获取url列表和时间列表
        title_list, url_list = self.get_url_list()
        
		# 遍历url列表，发送请求，获取响应
        for url in url_list[:1]:
            num = url_list.index(url)
           	# 解析url，获得html
            html_str = self.parse_url(url)
            # 获取内容
            html = etree.HTML(html_str)
            other = html.xpath("//*[@id=\"js_content\"]//text()")
            # list转字符串
            others = '\n'.join(other)
            # 标题
            name = title_list[num]
            print(num+1, name, others)
			
if __name__ == '__main__':
    weixin_spider = WeixinSpider_1()
    weixin_spider.run()





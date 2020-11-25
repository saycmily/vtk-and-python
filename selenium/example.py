# IPython2 测试代码
import time
# 导入 webdriver
from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
option = webdriver.ChromeOptions()
# option.add_argument('--headless')    #没有窗口的模式
# option.add_argument('--start-maximized')    #窗口最大化
option.add_argument('--window-size=1024,768')    #设置窗口大小
# option.add_argument('--disable-infobars')    #在窗口上不出现‘自动化测试’提示
# option.add_argument('--blink-settings=imagesEnabled=false')    #不显示图片
driver = webdriver.Chrome(options=option)

driver.get("http://www.baidu.com/")
time.sleep(2)
data = driver.find_element_by_id("wrapper").text
print(data)
print(driver.title)
driver.save_screenshot("baidu.png")
# 输入内容
driver.find_element_by_id("kw").send_keys(u"韩国女团")
# 点击
driver.find_element_by_id("su").click()
time.sleep(3)
driver.save_screenshot("1.png")

# 网页源代码
# print(driver.page_source)
# 页面Cookie
# print(driver.get_cookies())

driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
driver.find_element_by_id("kw").send_keys(u"后背摇")
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(2)
driver.save_screenshot("2.png")
driver.find_element_by_id("kw").clear()
print(driver.current_url)
# 关闭页面
# driver.close()
# 关闭浏览器
# driver.quit()

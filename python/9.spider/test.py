from selenium import webdriver

# 创建chrome参数对象
opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
opt.headless = True
# 创建chrome无界面对象
driver = webdriver.Chrome(options=opt)
# 访问百度
driver.get('https://baidu.com/')
print(driver.page_source)

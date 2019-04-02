

from selenium import webdriver
import time
import os
from Common import Assert

assertions = Assert.Assertions


#打开浏览器
#确定chromedriver.exe的位置
class TestFirstUIdemo:
    def test_testdome1(self):
        # 打开浏览器
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")
        #打来浏览器
        print(driver_path)
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.implicitly_wait(8)  # 设置隐式时间等待
        time.sleep(2)
        #打开网址
        driver.get("http://192.168.60.132/#/login")
        #输入用户名

        username = driver.find_element_by_xpath('//input [@name="username"]')
        username.clear()
        username.send_keys('admin')
        time.sleep(2)
        #输入密码
        password = driver.find_element_by_xpath('//input[@name="password"]')
        password.clear()
        password.send_keys('123456')
        time.sleep(2)
        #点击登录
        login = driver.find_element_by_xpath('(//span[contains(text(),"登录")])[1]')
        login.click()
        time.sleep(2)
        # 点击商品
        shangpin = driver.find_element_by_xpath('//span[contains(text(),"商品")]')
        shangpin.click()
        time.sleep(2)
        #点击添加商品
        tjsp = driver.find_element_by_xpath('//span[contains(text(),"添加商品")]')
        tjsp.click()
        time.sleep(2)
        #点击商品分类下拉框
        spxl = driver.find_element_by_xpath('//span[@class="el-cascader__label"]')
        spxl.click()
        time.sleep(2)
        #点击服装//li[@aria-expanded="true"]
        #点击外套//li[contains(text(),"外套")]
        #点击商品名称//div[@class="el-input el-input--small"]
        #点击副标题//div[@class="el-form-item is-error is-required el-form-item--small"][2]
        #点击商品品牌
        #点击商品介绍
        #点击商品介绍
        #点击货号
        #点击售价
        #点击市场价
        #点击商品库存
        #计量单位
        #点击商品重量
        #排序点击排序

        #点击营销
        # yingxiao = driver.find_element_by_xpath('//span[contains(text(),"营销")]')
        # yingxiao.click()
        # time.sleep(2)
        # #点击优惠劵列表
        # youhui = driver.find_element_by_xpath('//span[contains(text(),"优惠券列表")]')
        # youhui.click()
        # time.sleep(2)
        # #输入优惠券名称
        # mingcheng = driver.find_element_by_xpath('//input[@placeholder="优惠券名称"]')
        # mingcheng.clear()
        # mingcheng.send_keys('小米手机')
        # time.sleep(2)
        # #点击查询搜索
        # sousuo = driver.find_element_by_xpath('//span[contains(text(),"查询搜索")]')
        # sousuo.click()
        # time.sleep(2)
        # 断言
        #assertions.assert_in_text(driver.page_source,'首页')
        #退出浏览器
        #driver.quit()

































































































































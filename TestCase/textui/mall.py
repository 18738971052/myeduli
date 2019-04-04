from selenium import webdriver
import time
import os
from Common.Assert import Assertions
from Common.baseui import baseUI
class TestFstUIDemo:
        def test_6(self, driver):
            driver.get("http://192.168.60.132/#/login")
            base = baseUI(driver)
            base.send_keys("输入用户名", "//input[@name='username']", "admin")
            # 数据密码
            base.send_keys("输入密码", "//input[@name='password']", "123456")
            # 点击登录
            base.click("点击登录","//span[contains(text(),'登录')]")
            #点击订单
            base.click("点击订单","(//span[contains(text(),'订单')])[1]")
            #点击订单列表
            base.click("点击订单列表","//span[contains(text(),'订单列表')]")
            #点击订单状态
            base.click("点击订单状态","(//input[@readonly='readonly'])[1]")
            #点击代发货
            base.click("点击代发货","//span[contains(text(),'待发货')]")
            #点击查询搜索
            base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
            #点击订单发货
            base.click("点击订单发货","//span[contains(text(),'订单发货')]")
            #点击配送方式下拉框
            base.click("点击配送方式下拉框","//input[@placeholder='请选择物流公司']")
            #点击顺丰快递
            base.click("点击顺丰快递","//span[contains(text(),'顺丰快递')]")
            #点击确定
            base.click("点击确定","//span[contains(text(),'确定')]")
            time.sleep(2)
            #确定修改
            base.click("确定修改","(//span[contains(text(),'确定')])[2]")
            time.sleep(3)
            #捕捉发货成功/html[@class=' ']/body/div[@class='el-message el-message--success']
            print(driver.page_source)
































































































































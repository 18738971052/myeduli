from selenium import webdriver
import time
import os
from Common.Assert import Assertions
from Common.baseui import baseUI
class TestFirstUIDemo:
        def test_6(self, driver):
            driver.get("http://192.168.60.132/#/login")
            base = baseUI(driver)
            base.send_keys("输入用户名", "//input[@name='username']", "admin")
            # 数据密码
            base.send_keys("输入密码", "//input[@name='password']", "123456")
            # 点击登录
            base.click("点击登录", "//span[contains(text(),'登录')][1]")
            # 点击商品(//span[contains(text(),'商品')])[1]
            base.click("点击营销", "(//span[contains(text(),'营销')])[1]")
            #点击优惠券列表
            base.click("点击优惠券列表","//span[contains(text(),'优惠券列表')]")
            #点击编辑
            base.click("点击编辑","(//span[contains(text(),'编辑')])[1]")
            #点击提交
            base.click("点击提交","(//span[contains(text(),'提交')])")
            #点击确定
            base.click("点击确定","//span[contains(text(),'确定')]")
            #断言
            driver.find_element_by_xpath(
                "/html[ @class =' ']/body/div[@ class ='el-message el-message--success']/p[@ class ='el-message__content']")







































































































































from selenium import webdriver
import time
import os
from Common.Assert import Assertions
from Common.baseui import baseUI
class Test1:
        def test_2(self,driver):
                driver.get("http://192.168.60.132/#/login")
                base = baseUI(driver)
                base.send_keys("输入用户名","//input[@name='username']","admin")
                # 数据密码
                base.send_keys("输入密码","//input[@name='password']", "123456")
                # 点击登录
                base.click("点击登录","//span[contains(text(),'登录')][1]")
                #点击商品(//span[contains(text(),'商品')])[1]
                base.click("点击商品","(//span[contains(text(),'商品')])[1]")
                # 点击添加商品
                base.click("点击添加商品","//span[contains(text(),'添加商品')]")
                #点击商品分类
                base.click("点击商品分类","//label[contains(text(),'商品分类：')]/following-sibling::div/span")
                # 选择手机数码
                base.click("选择手机数码","//li[contains(text(),'手机数码')]")
                # 选择手机通讯录
                base.click("选择手机通讯录","//li[contains(text(),'手机通讯')]")
                #点击商品名称
                base.send_keys("商品名称","//label[contains(text(),'商品名称：')]/following-sibling::div//input","华为")
                # 副标题
                base.send_keys("副标题","//label[contains(text(),'副标题')]/following-sibling::div//input","华为")
                # 选择品牌
                base.click("选择品牌","//input[@placeholder='请选择品牌']")
                # 选择华为
                base.click("华为","//span[contains(text(),'华为')]")
                # 点击下一步
                base.click("点击下一步","//span[contains(text(),'下一步，填写商品促销')]")
                # 填写属性
                base.click("填写属性","//span[contains(text(),'下一步，填写商品属性')]")
                #切换到iframe
                base.switch_to_frame("切换到iframe","//iframe[contains(@id,'vue-tinymce')]")
                #填写规格参数
                base.send_keys("填写规格参数","//body[@id='tinymce']","测试一下")
                driver.switch_to.default_content()
                # 选择商品关联
                base.click("选择商品关联","//span[contains(text(),'下一步，选择商品关联')]")
                # 完成商品
                #base.click("完成商品","//span[contains(text(),'完成，提交商品')]")
                # 确定
                #base.click("完成","//span[contains(text(),'确定')]")

                # driver.quit()
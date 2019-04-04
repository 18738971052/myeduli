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
                time.sleep(2)
                #填写规格参数
                base.send_keys("填写规格参数","//body[@id='tinymce']","测试一下")
                driver.switch_to.default_content()
                #base.switch_to.default_content()
                time.sleep(2)
                # 选择商品关联
                base.click("选择商品关联","//span[contains(text(),'下一步，选择商品关联')]")
                time.sleep(2)
                # 完成商品
                #base.click("完成商品","//span[contains(text(),'完成，提交商品')]")
                # 确定
                #base.click("完成","//span[contains(text(),'确定')]")

                # driver.quit()


class TestFirstUIDemo:
    def test_3(self, driver):
        driver.get("http://192.168.60.132/#/login")
        base = baseUI(driver)
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        # 数据密码
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')][1]")
        # 点击商品(//span[contains(text(),'商品')])[1]
        base.click("点击营销", "(//span[contains(text(),'营销')])[1]")
        # 点击优惠券列表
        base.click("点击优惠券列表", "//span[contains(text(),'优惠券列表')]")
        # 点击编辑
        base.click("点击编辑", "(//span[contains(text(),'编辑')])[1]")
        #点击优惠券类型
        base.click("点击优惠券类型","//input[@placeholder='请选择']")
        #点击购物用券
        base.click("点击购物用券","//span[contains(text(),'购物赠券')]")
        #输入优惠券名称
        base.send_keys("输入优惠券名称","//div[@class='input-width el-input el-input--small']/input","优惠")
        #选择适用平台
        base.click("选择适用平台","(//div[@class='el-input el-input--small el-input--suffix'])[2]")
        #点击全平台
        base.click("点击全平台","//li[@class='el-select-dropdown__item selected']")
        #输入总发行量
        #输入面额
        base.send_keys("输入面额", "//input[@placeholder='面值只能是数值，限2位小数']")

        #输入每人限领(//input[@placeholder="只能输入正整数"])[2]
        #输入使用门槛
        #输入有效期
        #填写备注
        # 点击提交
        base.click("点击提交", "(//span[contains(text(),'提交')])")
        # 点击确定
        base.click("点击确定", "//span[contains(text(),'确定')]")
        # 找到提示框的xpath
        print(driver.page_source)
        text = base.get_text("获取页面展示文本", "//div[@role='alert']/p")
        print(driver.page_source)
        # print(text)
        # base.assert_in_text("text","修改成功")
        time.sleep(4)


    def test_demo5(self,driver):
        base = baseUI(driver)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名//input[@name='username']
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        # 输入密码//input[@name='password']
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录(//span[contains(text(),'登录')])[1]
        base.click('点击登录', "(//span[contains(text(),'登录')])[1]")
        #点击订单//span[text()='订单']
        base.click("点击订单","//span[text()='订单']")
        #点击订单列表(//span[text()='订单列表'])[1]
        base.click("点击订单列表", "(//span[text()='订单列表'])[1]")
        #点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        #点击待发货//span[text()='待发货']
        base.click("点击待发货", "//span[text()='待发货']")
        #点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        #记录第一条的编号//tbody/tr[1]/td[2]/div
        num = base.get_text('获取编号',"//tbody/tr[1]/td[2]/div")
        order_num = base.get_text("获取订单编号","//tbody/tr[1]/td[3]/div")
        #点击第一条订单发货//tbody/tr[1]/td[10]/div/button[3]
        base.click("点击第一条订单发货","//tbody/tr[1]/td[10]/div/button[3]")
        #点击配送方式//input[@placeholder='请选择物流公司']
        base.click("点击配送方式","//input[@placeholder='请选择物流公司']")
        #点击圆通快递//span[text()='圆通快递']
        base.click("点击圆通快递","//span[text()='圆通快递']")
        #输入物流单号//tbody/tr/td[7]//input
        base.send_keys("输入物流单号","//tbody/tr/td[7]//input","123456789")
        #点击确定//span[text()='确定']
        base.click("点击确定","//span[text()='确定']")
        #确认(//span[contains(text(),'确定')])[2]
        base.click("确认","(//span[contains(text(),'确定')])[2]")
        #获取提示框文本//div[@role='alert']/p
        text = base.get_text("获取提示框文本","//div[@role='alert']/p")
        #断言
        Assertion.assert_in_text(text,'发货成功')
        # 点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        # 点击已发货//span[text()='待发货']
        base.click("点击已发货", "//span[text()='已发货']")
        #输入订单编号//input[@placeholder='订单编号']
        base.send_keys("输入订单编号","//input[@placeholder='订单编号']",order_num)
        # 点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        #定位到刚才发货的订单
        time.sleep(1)
        #通过xpath定位到一组元素，存到一个list中
        nums = driver.find_elements_by_xpath("(//tbody)[1]/tr/td[2]")
        #存放是否能找到编号 找到true  未找到 false
        b = False
        #遍历上边的list
        for n in nums:
            #n.text取出元素的可视文本
            print(n.text)
            #判断可视文本是否与发货订单的编号相同
            if n.text ==num:
                #如果相同，就讲true赋值给b
                b = True
        #断言，订单状态转换是否正确
        assert True == b
        time.sleep(3)





    def test_demo100(self,driver):
        base = baseUI(driver)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名//input[@name='username']
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        # 输入密码//input[@name='password']
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录(//span[contains(text(),'登录')])[1]
        base.click('点击登录', "(//span[contains(text(),'登录')])[1]")
        #点击订单//span[text()='订单']
        base.click("点击订单","//span[text()='订单']")
        #点击订单列表(//span[text()='订单列表'])[1]
        base.click("点击订单列表", "(//span[text()='订单列表'])[1]")
        #点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        #点击待发货//span[text()='待发货']
        base.click("点击待发货", "//span[text()='待发货']")
        #点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        #记录第一条的编号//tbody/tr[1]/td[2]/div
        num = base.get_text('获取编号',"//tbody/tr[1]/td[2]/div")
        order_num = base.get_text("获取订单编号","//tbody/tr[1]/td[3]/div")
        #点击第一条订单发货//tbody/tr[1]/td[10]/div/button[3]
        base.click("点击第一条订单发货","//tbody/tr[1]/td[10]/div/button[3]")
        #点击配送方式//input[@placeholder='请选择物流公司']
        base.click("点击配送方式","//input[@placeholder='请选择物流公司']")
        #点击圆通快递//span[text()='圆通快递']
        base.click("点击圆通快递","//span[text()='圆通快递']")
        #输入物流单号//tbody/tr/td[7]//input
        base.send_keys("输入物流单号","//tbody/tr/td[7]//input","123456789")
        #点击确定//span[text()='确定']
        base.click("点击确定","//span[text()='确定']")
        #确认(//span[contains(text(),'确定')])[2]
        base.click("确认","(//span[contains(text(),'确定')])[2]")
        #获取提示框文本//div[@role='alert']/p
        text = base.get_text("获取提示框文本","//div[@role='alert']/p")
        #断言
        Assertion.assert_in_text(text,'发货成功')
        # 点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        # 点击已发货//span[text()='待发货']
        base.click("点击已发货", "//span[text()='已发货']")
        #输入订单编号//input[@placeholder='订单编号']
        base.send_keys("输入订单编号","//input[@placeholder='订单编号']",order_num)
        # 点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        #定位到刚才发货的订单
        time.sleep(1)
        #通过xpath定位到一组元素，存到一个list中
        nums = driver.find_elements_by_xpath("(//tbody)[1]/tr/td[2]")
        #存放是否能找到编号 找到true  未找到 false
        b = False
        #遍历上边的list
        for n in nums:
            #n.text取出元素的可视文本
            print(n.text)
            #判断可视文本是否与发货订单的编号相同
            if n.text ==num:
                #如果相同，就讲true赋值给b
                b = True
        #断言，订单状态转换是否正确
        assert True == b
        time.sleep(3)


    def test_demo6(self,driver):
        #打开网址
        driver.get("http://192.168.60.132/#/login")
        base = baseUI(driver)
        #输入用户名//input[@name='username']
        #输入密码//input[@name='password']
        #点击确定//span[contains(text(),'登录')]
        #点击订单(//span[contains(text(),'订单')])[1]
        #点击订单列表//span[contains(text(),'订单列表')]
        #点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        #点击未发货//span[contains(text(),'待发货')]
        #点击查询搜索//span[contains(text(),'查询搜索')]
        #点击全选
        #点击批量操作
        #点击批量发货
        #点击确定
        #循环填写配送方式
        #循环填写订单编号
        #点击确定








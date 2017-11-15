from appium import webdriver
import unittest
from time import sleep
from nativeApp.back import backtoinit

from nativeApp.browser import FindElement
class Chrome(unittest.TestCase):
    def setUp(self):
        self.find=FindElement("com.android.chrome","com.google.android.apps.chrome.Main")

    # def testA_opentaobao(self):#打开淘宝网址
    #     find=self.find
    #     url=find.myfindId('com.android.chrome:id/url_bar')
    #     url.send_keys('http://www.taobao.com')
    #     find.returnDriver().press_keycode(66)#回车键
    # def testB_search(self):
    #     find=self.find
    #     url = find.myfindXpath('//android.widget.EditText[contains(@text,\'搜索或输入网址\')]')
    #     url.click()
    #     url.send_keys('http://www.baidu.com')
    #     find.returnDriver().press_keycode(66)
    #
    #     # 回车键
    #     d=find.returnDriver()
    #     # d.implicitly_wait(30)
    #     sleep(10)
    #     #回车后给3秒加载时间
    #     cons = d.contexts  # 获取上下文列表
    #     print(cons)
    #     # d._switch_to.context(cons[-1])
    #     for cons in d.contexts:
    #         if cons.lower().startswith('webview'):
    #             print(cons)
    #             d._switch_to.context(cons)
    #     find.myfindId('index-kw').send_keys('移动端自动化')
    #     find.myfindId('index-bn').click()
    def testC_clickMine(self):
        #点击我的
        find=self.find
        url = find.myfindXpath('//android.widget.EditText[contains(@text,\'搜索或输入网址\')]')
        url.click()
        url.send_keys('http://www.meituan.com')
        find.returnDriver().press_keycode(66)
        d=find.returnDriver()
        sleep(10)#同样给10秒网址加载时间
        for cons in d.contexts:
            if cons.lower().startswith('webview'):
                d._switch_to.context(cons)
                # print(d.current_url)获取当前的url

        find.myfindXpath('//*[@id="index"]/header/div[3]').click()


    def tearDown(self):
        #按back键退出acticity 使再次进入时是谷歌网址页面
        backtoinit(self.find.returnDriver())



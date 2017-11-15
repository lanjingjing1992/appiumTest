import unittest

from nativeApp.back import backtoinit
from nativeApp.browser import FindElement
from time import sleep

class math(unittest.TestCase):
    def setUp(self):
        self.find=FindElement('com.nwoolf.xy.p532','com.nwoolf.xy.p532.MainActivity')
    # def testA_clock(self):
    #     find=self.find
    #     find.myfindId('com.nwoolf.xy.p532:id/unlock_btn').click()
    #     find.myfindXpath('//android.widget.TextView[contains(@text,\'未购用户购买\')]').click()
    #     #输入账号
    #     find.myfindId('com.nwoolf.xy.p532:id/et_account').send_keys('15901337131')
    #     #输入密码
    #     find.myfindId('com.nwoolf.xy.p532:id/et_password').send_keys('123456')
    #     #登陆
    #     find.myfindId('com.nwoolf.xy.p532:id/btn_login').click()
    #     sleep(3)#休眠3秒
    def mine(self,find):

        find.myfindId('com.nwoolf.xy.p532:id/option_btn').click()  # 点击我的
        # 点击关于
        find.myfindXpath('//android.widget.TextView[contains(@text,\'关于\')]').click()

    def testB_Mine(self):
        find = self.find
        self.mine(find)
        #检查文案
        str=find.myfindId('com.nwoolf.xy.p532:id/about_app_version_tv').text
        print(str)#人教版小学数学三年级下册
        self.assertEqual(str,'人教版小学数学三年级下册')
    def testC_checktext(self):#检查关于页面所有的文案
        find=self.find
        self.mine(find)
        textview=find.myfindClassNames('android.widget.TextView')
        for t in textview:
            print(t.text)
        self.assertEqual(textview[1].text,'人教版小学数学 三年级下册  v3.0.1')
        self.assertEqual(textview[2].text,'QQ：3354834044')
        self.assertEqual(textview[3].text,'Email：ihaobaba@126.com')
    def tearDown(self):
        backtoinit(self.find.returnDriver())

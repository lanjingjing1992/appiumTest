import unittest
from nativeApp.browser import FindElement
from nativeApp.back import backtoinit
from time import sleep

class Zhibo(unittest.TestCase):
    def setUp(self):
        self.find=FindElement('com.syoogame.yangba','com.syoogame.yangba.MainActivity')

    def testA_login(self):
        find=self.find
        find.myfindXpath('//android.widget.TextView[contains(@text,\'我的\')]').click()#点击我的
        find.myfindXpath('//android.widget.TextView[contains(@text,\'登录/注册\')]').click()#点击登陆注册
        #点击qq登陆
        print('4444')
        find.myfindXpath('//android.widget.TextView[contains(@text,\'QQ\')]').click()
        #授权并登陆
        print('2222')
        find.myfindXpath('//android.widget.Button[contains(@text,\'登录\')]').click()
        # find.myfindId('com.tencent.mobileqq:id/name').click()#注意页面上的id都是一样的，不是唯一id，不用使用
        print('3333')

        sleep(3)#休眠3秒
    def tearDown(self):
        backtoinit(self.find.returnDriver())


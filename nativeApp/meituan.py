import unittest
from nativeApp.browser import FindElement
from HTMLTestRunner import HTMLTestRunner

class Meituan(unittest.TestCase):
    def setUp(self):
        self.myfind=FindElement('com.sankuai.meituan','com.sankuai.meituan.activity.Welcome')

    def testA_login(self):
        #点击我的
        find = self.myfind
        find.myfindXpath('//android.widget.TextView[contains(@text,\'我的\')]').click()  # 点击我的
        find.myfindId('com.sankuai.meituan:id/avatar').click()#点击头像登陆
        #比较注册文本是否一致，一致的话则跳转成功
        regist1=find.myfindId('com.sankuai.meituan:id/action_signup').text
        self.assertEqual(regist1,'注册')
        #点击返回
        find.myfindClassName('android.widget.ImageButton').click()
        find.myfindId('com.sankuai.meituan:id/user_name').click()#点击文本登陆
        regist2 = find.myfindId('com.sankuai.meituan:id/action_signup').text
        self.assertEqual(regist2, '注册')
    def testB_distance(self):
        find = self.myfind
        # 点击我的
        find.myfindXpath('//android.widget.TextView[contains(@text,\'我的\')]').click()
        find.myfindId('com.sankuai.meituan:id/avatar').click()  # 点击头像登陆
        regist = find.myfindId('com.sankuai.meituan:id/action_signup').text
        self.assertEqual(regist, '注册')#文案是否一致
        try:
            find.myfindXpath('//android.widget.TextView[contains(@text,\'微信登陆\')]')
        except:
            print('没有找到微信登陆的控件')
        usepthonelogin=find.myfindId('com.sankuai.meituan:id/passport_button_meituan').text
        self.assertEqual(usepthonelogin,'使用手机号登录')#判断文案是否一致
        useothers=find.myfindId('com.sankuai.meituan:id/passport_button_other').text
        self.assertEqual(useothers,'使用其他方式登录')
    def testC_assertequal(self):
        find = self.myfind
        # 点击我的
        find.myfindXpath('//android.widget.TextView[contains(@text,\'我的\')]').click()
        find.myfindId('com.sankuai.meituan:id/avatar').click()  # 点击头像登陆
        loginMode=find.myfindXpath('//android.widget.TextView[contains(@text,\'推荐登录方式\')]').text
        self.assertEqual('推荐登陆方式',loginMode)

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Meituan('testA_login'))
    suite.addTest(Meituan('testB_distance'))
    suite.addTest(Meituan('testC_assertequal'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=open('result.html','w+'),title='lanjingjing',description='这是我的测试报告')
    runner.run(suite)






    def tearDown(self):
        pass
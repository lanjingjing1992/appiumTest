import unittest
from nativeApp.browser import FindElement
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        #检查美团首页的分类是否全部显示
    def testD_Firstpageimgs(self):
        find = self.myfind
        meishi=find.myfindXpath('//android.widget.TextView[contains(@text,\'美食\')]')
        dianying=find.myfindXpath('//android.widget.TextView[contains(@text,\'电影\')]')
        jiudian=find.myfindXpath('//android.widget.TextView[contains(@text,\'酒店\')]')
        yule=find.myfindXpath('//android.widget.TextView[contains(@text,\'娱乐\')]')
        waimai=find.myfindXpath('//android.widget.TextView[contains(@text,\'外卖\')]')
        self.assertIsNotNone(meishi)
        self.assertIsNotNone(dianying)
        self.assertIsNotNone(jiudian)
        self.assertIsNotNone(yule)
        self.assertIsNotNone(waimai)
    def testE_guessYouLover(self):

        find=self.myfind
        #移动半个页面才能出来如下控件
        find.myTopScroll(1,'com.sankuai.meituan:id/actionbar_scan_iv')

        guess=find.myfindXpath('//android.widget.TextView[contains(@text,\'猜你喜欢\')]')


        for i in range(1000):
            find.myTopScroll(30)

            try:
                all=find.myfindXpath('//android.widget.TextView[contains(@text,\'查看全部\')]')
                # self.assertEqual(guess.text, '猜你稀饭')
                self.assertEqual(all.text, '查看全部')
                return
            except:
                pass









    def tearDown(self):
        pass



if __name__ == '__main__':
    suite=unittest.TestSuite()
    # suite.addTest(Meituan('testA_login'))
    # suite.addTest(Meituan('testB_distance'))
    # suite.addTest(Meituan('testC_assertequal'))
    # suite.addTest(Meituan('testD_Firstpageimgs'))
    suite.addTest(Meituan('testE_guessYouLover'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=open('result.html','w+'),title='lanjingjing',description='这是我的测试报告')
    runner.run(suite)







import unittest
from auto.browser import FindElement
class Meituan(unittest.TestCase):
    def setUp(self):
        self.myfind=FindElement('com.sankuai.meituan','com.sankuai.meituan.activity.Welcome')
    def testLogin(self):
        #点击我的
        find=self.myfind
        find.myfindXpath('//android.widget.TextView[contains(@text,\'我的\')]').click()#点击我的
        find.myfindId('com.sankuai.meituan:id/avatar').click()#点击头像登陆
        #比较注册文本是否一致，一致的话则跳转成功
        regist1=find.myfindId('com.sankuai.meituan:id/action_signup').text
        self.assertEqual(regist1,'注册')
        #点击返回
        find.myfindClassName('android.widget.ImageButton').click()
        find.myfindId('com.sankuai.meituan:id/user_name').click()#点击文本登陆
        regist2 = find.myfindId('com.sankuai.meituan:id/action_signup').text
        self.assertEqual(regist2, '注册')
    # def testDistance(self):
    #     find=self.myfind
    #     find.myfindId('com.sankuai.meituan:id/tab_icon').click()
    #     find.myfindId('com.sankuai.meituan:id/avatar').click()  # 点击头像登陆
    #     regist = find.myfindId('com.sankuai.meituan:id/action_signup').text
    #     self.assertEqual(regist, '注册')#文案是否一致
    #     try:
    #         find.myfindXpath('//android.widget.TextView[contains(@text,\'微信登陆\')]')
    #     except:
    #         print('没有找到微信登陆的控件')
    #     usepthonelogin=find.myfindId('com.sankuai.meituan:id/passport_button_meituan').text
    #     self.assertEqual(usepthonelogin,'使用手机号登录')#判断文案是否一致
    #     useothers=find.myfindId('com.sankuai.meituan:id/passport_button_other').text
    #     self.assertEqual(useothers,'使用其他方式登录')
    # def testAssetequal(self):
    #     find=self.myfind
    #     print(find.myfindXpath('//android.widget.TextView[contains(@text,\'推荐登陆方式\')]').text)





    def tearDown(self):
        pass
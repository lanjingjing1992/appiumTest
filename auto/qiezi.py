
from auto.browser import FindElement
import unittest
class qiezi(unittest.TestCase):
    def setUp(self):#导航页
        self.myfind=FindElement('com.qiezzi.eggplant','com.qiezzi.eggplant.base.WelcomeActivity')

    def testExperience(self):#立即体验
        self.myfind.myScroll(4, 'com.qiezzi.eggplant:id/btn_firstinstall_intent')
        self.myfind.myfindId('com.qiezzi.eggplant:id/btn_feel_right_now').click()

    def testlogin(self):#登陆或者注册页面
        myfind=self.myfind
        try:

            print('进入到登陆页面了')#已经登陆过了
            myfind.myimplicitly_wait(20)
            myfind.myfindId('com.qiezzi.eggplant:id/btn_main_my').click()#个人中心
            myfind.myfindId('com.qiezzi.eggplant:id/tv_fragment_hospital_state').click()#未认证
            myphton=myfind.myfindId('com.qiezzi.eggplant:id/tv_hospital_phone').click()
            myName=myfind.myfindName\
                ('com.qiezzi.eggplant:id/tv_hospital_contact').click()

            print(myphton.text)#我的手机号
            print(myName.text)#我的用户名
        except:
            print('从登陆页启动')#第一次登陆
            myfind.myfindId('com.qiezzi.eggplant:id/edt_frist_login_accout').send_keys('15901337131')
            myfind.myfindId('com.qiezzi.eggplant:id/edt_frist_login_password').send_keys('442131ljj')
            myfind.myfindId('com.qiezzi.eggplant:id/btn_frist_login_immediately').click()#登陆
    def tearDown(self):
            pass



#新页面--------------------------------------








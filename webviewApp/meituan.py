import unittest
from nativeApp.back import backtoinit
from nativeApp.browser import FindElement
from time import sleep
class MeiTuan(unittest.TestCase):
    def setUp(self):
        self.myfind = FindElement('com.sankuai.meituan', 'com.sankuai.meituan.activity.Welcome')#输入包名，启动activity的名字，进行初始化

    def testA_webview(self):#附近
        find=self.myfind
        find.myfindXpath('//android.widget.TextView[contains(@text,\'逛一逛\')]').click()
        d=self.myfind.returnDriver()#驱动
        cons=d.contexts
        print(cons)#打印出来只有native_app 解决办法参考连接https://www.cnblogs.com/sao-fox/p/6396984.html
        for con in cons:
            if con.lower().startswith('webview'):
                d._switch_to.context(con)
                print('success')
        #向左滑动
        find.myLeftScroll(6)

        sleep(5)
    def tearDown(self):
        backtoinit(self.myfind.returnDriver())





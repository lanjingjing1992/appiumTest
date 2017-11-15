import unittest
from nativeApp.back import backtoinit
from nativeApp.browser import FindElement
from time import sleep

class Duodian(unittest.TestCase):
    def setUp(self):
        self.find=FindElement('com.wm.dmall','com.wm.dmall.LaunchActivity')
    def testA_Scroll(self):
        find=self.find
        find.myfindXpath('//android.widget.TextView[contains(@text,\'多点超市\')]')
        find.myTopScroll(2)
        sleep(2)
        find.myLeftScroll(4)#注意滑动的区域不要超过给定的区域

    def tearDown(self):
        pass
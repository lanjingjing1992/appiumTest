from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class FindElement(object):
    def __init__(self,appPackage,appActivity):
        self.desired_capabilities = {}
        self.desired_capabilities['platformName'] = 'Android'
        self.desired_capabilities['platformVersion'] = '6.0.1'
        self.desired_capabilities['deviceName'] = '32d0d84a'
        self.desired_capabilities['appPackage'] = appPackage
        self.desired_capabilities['appActivity'] = appActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_capabilities)
        self.driver.implicitly_wait(30)
        #宽高：1080 1920

        self.width=self.driver.get_window_size()['width']
        self.height=self.driver.get_window_size()['height']

        print('连接成功')
    def myfindId(self,id):
        try:
            ID=(By.ID,id)
            WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(ID))
            return self.driver.find_element_by_id(id)
        except:
            pass
    def myfindClassName(self,className):
        try:
            classN=(By.CLASS_NAME,className)
            WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(classN))
            return self.driver.find_element_by_class_name(className)
        except:
            pass

    def myfindName(self,name):
        try:
            NAME=(By.NAME,name)
            WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(NAME))
            return self.driver.find_element_by_name(name)
        except:
            pass
    def myfindXpath(self,xpath):
        try:
            XPATH=(By.XPATH,xpath)
            WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(XPATH))
            return self.driver.find_element_by_xpath(xpath)
        except:
            pass

    def mytimeSleep(self,number):
        time.sleep(number)
    def mycloseChrome(self):
        self.driver.quit()

    def myimplicitly_wait(self,number):
        self.driver.implicitly_wait(number)
    def myScroll(self,number,id):
        ID=(By.ID,id)
        WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(ID))


        for i in range(number):
            self.driver.implicitly_wait(30)
            x1 = int(self.width * 0.75)
            x2 = int(self.width * 0.05)
            y = int(self.height * 0.5)
            self.driver.swipe(x1, y, x2, y, 1000)












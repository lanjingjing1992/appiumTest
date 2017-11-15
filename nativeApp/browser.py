from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
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
    def returnDriver(self):

        return  self.driver
    def myfindId(self,id):
        try:
            ID=(By.ID,id)
            WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(ID))
            return self.driver.find_element_by_id(id)
        except:
            pass
    def myFindIds(self,id):
        try:
            ID = (By.ID, id)
            WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_all_elements_located_located(ID))
            return self.driver.find_elements_by_id(id)
        except:
            pass

    def myfindClassNames(self,className):
        try:
            classN=(By.CLASS_NAME,className)
            WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(classN))
            return self.driver.find_elements_by_class_name(className)
        except:
            pass

    def myfindClass(self, className):
        try:
            classN = (By.CLASS_NAME, className)
            WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(classN))
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
    def myLeftScroll(self,number,id=None):
        if id!=None:
            ID=(By.ID,id)
            WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(ID))


        for i in range(number):
            print('第%s次滑动'%(i+1))
            time.sleep(2)
            x1 = int(self.width*0.9)
            x2 = int(self.width * 0.05)#偏移量
            y = int(self.height * 0.75)
            self.driver.swipe(x1, y, x2, y, 1000)

    def myTopScroll(self, number,id=None):#number是滑动几次  id是页面上出现那个元素时开始滑动
        if id!=None:
            ID = (By.ID, id)
            WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(ID))

        for i in range(number):

            self.driver.implicitly_wait(30)
            x = int(self.width*0.5)
            y1 = int(self.height * 0.75)
            y2 = int(self.width * 0.25)

            self.driver.swipe(x, y1, x, y2, 1000)













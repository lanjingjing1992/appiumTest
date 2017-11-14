from appium import webdriver
desired_capabilities = {}
desired_capabilities['platformName'] = 'Android'
desired_capabilities['platformVersion'] = '6.0.1'
desired_capabilities['deviceName'] = '32d0d84a'
desired_capabilities['appPackage'] = "com.android.chrome"
desired_capabilities['appActivity'] = "com.google.android.apps.chrome.Main"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

url = driver.find_element_by_id('com.android.chrome:id/url_bar')
url.send_keys('http://www.baidu.com')
driver.press_keycode(66)  # 回车键

cons = driver.contexts  # 获取上下文列表
print(cons)
# d._switch_to.context(cons[-1])
for cons in driver.contexts:
    if cons.lower().startswith('webview'):
        print(cons)
        driver.switch_to.context(cons)
        driver._switch_to.context(cons)
#
driver.find_element_by_id('index-kw').send_keys('appium')
driver.find_element_by_id('index-bn').click()
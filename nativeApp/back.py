def backtoinit(driver):
    for i in range(10):  # 按back键退出acticity 使再次进入时是谷歌网址页面
        driver.keyevent(4)
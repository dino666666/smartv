# -*- coding: utf-8 -*-

import time,os

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from Common.Globe_Path.locator_appium import settings

class Base(object):
    def __init__(self,driver,adb,do_log,do_logcat):
        self.driver = driver
        self.adb = adb
        self.do_log = do_log
        self.do_logcat = do_logcat

    def Open(self):
        # 打开测试APP，测试前的准备
        # 端口可能被占用
        # netstat -ano|findstr 4723
        # taskkill - PID xxx - F
        desired_caps={'deviceName': 'G6210070B1FP00033',
                      'platformVersion': '10',
                      'udid': 'G6210070B1FP00033',
                      'platformName': 'Android',
                      'appPackage': 'com.heytap.tv.launcher',
                      'appActivity': 'com.oneplus.tv.launcher2.HomeLauncher',
                      # 'appPackage': 'com.heytap.tv.support',
                      # 'appActivity': 'com.heytap.tv.support.SourceListActivity',
                      'noReset': True,
                      'unicodeKeyboard': True,
                      'MobileCapabilityType.CLEAR_SYSTEM_FILES': True,
                      'newCommandTimeout': 3600,
                      'automationName': 'UiAutomator1',
                      'systemPort': 8200}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def start_app(self,app_package,app_activity):
        #启动app
        self.driver.start_activity(app_package,app_activity)


    def Quit(self):
        self.driver.quit()
        #测试完成需要还原环境

    @property
    def width(self):
        return self.driver.get_window_size()['width']

    @property
    def height(self):
        return self.driver.get_window_size().get('height')

    def swipe_top(self, x1=0.5, y1=0.9, x2=0.5, y2=0.2, duration=2000):
        self.driver.swipe(self.width * x1, self.height * y1, self.width * x2, self.height * y2, duration=duration)
        time.sleep(1)

    def find_element_click(self,locator):
        '''查找元素并点击'''
        time.sleep(1)     #休眠一秒防止页面没有刷新出来
        try:
            ele = self.find_element(locator)
            ele.click()
        except Exception as e:
            print("点击报错了：{}".format(e))

    # def find_element_new(self,ele):
    #     WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(MobileBy.ID,ele))
    #     self.driver.find_element_by_id(ele).click()

    def find_element(self, locator, timeout=10,poll_frequency=0.5,ignored_exceptions=None):
        '''查找元素
        :param locator:
        :param number: 最长超时时间，默认以秒为单位
        :param poll_frequency:检测的间隔步长，默认为0.5s
        :param ignored_exceptions:超时后的抛出的异常信息，默认抛出NoSuchElementExeception异常
        :return:
        '''
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            print("发现元素：{}".format(locator[1]))
            time.sleep(1)
            return element
        except Exception as e:
            print("元素为空:{}".format(e))
            return False

    def long_press(self, element):
        # 根据元素进行长按(能用元素最好用元素，用坐标可能存在兼容问题)
        action = TouchAction(self.driver)
        # 5000是设置的长按时间（单位/毫秒）
        action.long_press(element).wait(1000).release().perform()
        # 根据坐标进行长按
        # action = TouchAction(self.driver)
        # action.long_press(x=, y=).wait(5000).release().perform()

    def double_click(self, element):
      action = TouchAction(self.driver)
      action.press(element).release().press(element).release().perform()
      # action.press(element).release().press(element).release().perform()
      print('double click element({})', element)

    def driver_screenshot(self, pic_name, pic_file):
        # # 截图
        shot_file_name = "{}.png".format(pic_name + time.strftime("%Y%m%d_%H%M%S", time.localtime()))
        name = os.path.join(pic_file, shot_file_name)
        try:
            a = os.popen('adb devices').read()
            print(a)
            self.driver.get_screenshot_as_file(name)
        except Exception as e:
            print('截图失败,错误为{}'.format(e))
        return name


if __name__ == '__main__':
    locator = (MobileBy.XPATH,'//*[@text="已连接"]')
    d = Base('device','driver','do_log','do_logcat')
    print(1)
    d.Open()
    print(2)
    time.sleep(5)
    d.find_element_click(locator)
    print(4)
    d.Quit()
    print(5)







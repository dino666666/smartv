# -*- coding: utf-8 -*-

import time
import uiautomator2 as u2
from Common.Globe_Lib.Adbevent import ADB

class Base(object):
    def __init__(self,device,driver,adb,do_log,do_logcat):
        self.d = driver
        self.device = device
        self.adb = adb
        self.do_log = do_log
        self.do_logcat = do_logcat

    def wait_find_element_click(self,locator,timeout=20):
        '''
        :param locator: 传入元组
        :param timeout: 超时时间
        :return:
        '''
        try:
            ele = self.d.xpath(locator[1]).wait(timeout)
            self.click_smart(locator)
        except Exception as e:
            print("没有找到元素:{}".format(e))

    def find_element(self,locator,timeout=5):
        try:
            ele = self.d.xpath(locator[1]).wait(timeout)
            if ele:
                return True
            else:
                return False
        except Exception as e:
            print("没有找到元素:{}".format(e))

    def click_smart(self,locator):
        '''智能点击'''
        self.d(text=locator[0]).click_gone(maxretry=3, interval=1.0)

    def click(self,locator):
        self.d.xpath(locator[1]).click()

    def scoll_smark_click(self,locator,times=10):
        try:
            for i in range (times):
                ele = self.d.xpath(locator[1]).wait(timeout=1)
                if ele:
                    self.click_smart(locator)
                    break
                self.scroll(locator)
        except Exception as e:
            print("当前页面下没有找到元素，错误信息:{}".format(e))

    def scroll(self,locator):
        self.d(scrollable=True).scroll.to(text=locator[0])

    def screencap(self,path):
        self.d.screenshot(path)

    def record_start(self,path):
        self.d.screenrecord(path)

    def record_stop(self):
        self.d.screenrecord.stop()

    def app_start(self,app,stop=True,activity=None):
        self.d.app_stop(app)
        if stop:
            self.d.app_start(app,activity)
        else:
            self.d.app_start(app,activity,stop=False)
        app_pid=self.d.app_wait(app, 10, front=False)

    def server_stop(self):
        self.d.service("uiautomator").stop()

    def app_stop(self,app):
        self.d.app_stop(app)


if __name__ == '__main__':
    device = "00000A091A2009E01"
    path = "D:\\2_Log\\zhang.png"
    app = "com.heytap.tv.filebrowser"
    driver = u2.connect(device)
    adb = ADB(device)
    driver.debug = True
    d = Base(device=device,driver=driver,adb=adb,do_log="do_log",do_logcat="do_logcat")
    # d.app_start(app,stop=True)
    print(driver.info)
    # if d.find_element(Antutu.Antutu_13,timeout=3):
    #     print("Antutu_13能被识别")
    #     adb.back(1,2)
    # else:
    #     print("Antutu_13不能被识别")


    d.server_stop()
# -*- coding: utf-8 -*-
import time
import os

from Common.Globe_Path.locator_appium import USB_Play_Locator, Size_Window, WIFI_Locator, APP_Locator, HDMI_Locator, vedioplayer
from Common.Globe_Lib.Base_appium import Base

class Wifi_Page(Base):
    sub_locator = USB_Play_Locator
    size_window_locator = Size_Window
    app_locator = APP_Locator
    wifi_locator = WIFI_Locator
    # wifi_page
    def wifi_ping(self, device, driver, num, picturepath):
        for i in range(9):
            time.sleep(1)
            command1 = 'adb -s  ' + device + ' shell  ping -c 3 www.baidu.com'
            command2 = 'adb -s  ' + device + ' shell  ping -c 3 192.168.1.1'
            network1 = os.popen(command1).read()
            network2 = os.popen(command2).read()
            if ("ttl" in network1) or ("ttl" in network2):
                print("第 " + str(num) + " 轮测试网络ping成功")
                return True
            if i == 8:
                print('wifi图标显示异常，第 ' + str(num) + ' 轮ping网络失败')
                # 获取异常连接图片
                pt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
                name1 = 'Wifi_DC_第' + str(num) + "轮_" + str(pt) + 'ping网络失败.png'
                name = os.path.join(picturepath, name1)
                driver.get_screenshot_as_file(name)
                time.sleep(3)

    def wifi_text(self):
        if self.find_element(WIFI_Locator.net_wifi_status,timeout=20):
            return True
        else:
            print("wifi连接UI显示异常")
            return False


    def wifi_setting(self,project):
        if project == '9632':
            self.adb.up(1,3)
            self.adb.right(1, 2)
            self.adb.ok(1, 2)
            time.sleep(3)
            self.adb.up(5,2)
            time.sleep(2)
        elif project == '9612':
            pass
# -*- coding: utf-8 -*-
import os
import time

import pytest
from Common.Globe_Api.Wifi_Page import Wifi_Page

class Test_wifi_dc():
    # @pytest.mark.usefixtures("start_app_function")
    @pytest.mark.parametrize('num',range(1,10001))
    def test_wifi_dc(self, num, setup_wifi_dc, init_data):
        driver = setup_wifi_dc
        do_log,adb,picture_path,error_path,record_path,tombstones_path,anr_path,do_logcat\
            ,device = init_data
        wifi_driver = Wifi_Page(driver,adb,do_log,do_logcat)
        wifi_driver.wifi_setting("9632")
        if driver == 1:
            do_log.error("第 " + str(num) + " 次" + "测试driver错误")
            time.sleep(5)
        else:
            #打开logcat
            do_logcat.open('第' + str(num) + '轮')
            # 断言
            do_log.info("断言1：Ping www.baidu.com")
            Wifi_Ping = wifi_driver.wifi_ping(device, driver, num, picture_path)
            do_log.info("断言2：获取wifi 连接UI属性")
            Wifi_Text = wifi_driver.wifi_text()
            do_logcat.close()
            try:
                assert Wifi_Ping, "网络ping不通"
                assert Wifi_Text, "wifi未显示已连接"
                do_log.info('第{}轮测试成功,重启设备进入下一轮'.format(num))
            except Exception as e:
                do_log.info('第{}轮测试 Fail,获取错误信息'.format(num))
                adb.screencap(picture_path, module=num)
            # 开始关机
            adb.power_off()
            do_log.info('第{}轮测试成功'.format(num))
            adb.home()
            time.sleep(5)
            while True:
                time.sleep(1)
                result, window = adb.windows("Window")
                if result:
                    break
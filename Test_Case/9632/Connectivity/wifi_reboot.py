# -*- coding: utf-8 -*-
import datetime
import time

import pytest
from Common.Globe_Api.Wifi_Page import Wifi_Page

class Test_wifi_reboot():
    # @pytest.mark.usefixtures("start_app_function")
    @pytest.mark.parametrize('num', range(1, 100001))
    def test_wifi_reboot(self, num, init_driver, init_data):
        driver = init_driver
        do_log,adb,picture_path,error_path,record_path,tombstones_path,anr_path,do_logcat\
            ,device = init_data
        wifi_driver = Wifi_Page(driver,adb,do_log,do_logcat)
        wifi_driver.wifi_setting("9632")
        do_log.info("第 " + str(num) + " 次" + "测试程序启动")
        do_logcat.open('第' + str(num) + '轮wifi_reboot')
        # 断言
        do_log.info("断言1：Ping www.baidu.com")
        Wifi_Ping = wifi_driver.wifi_ping(device, driver, num, picture_path)
        do_log.info("断言2：获取wifi 连接UI属性")
        Wifi_Text = wifi_driver.wifi_text()
        try:
            assert Wifi_Ping, "网络ping不通"
            assert Wifi_Text, "wifi未显示已连接"
            do_log.info('第{}轮测试成功,重启设备进入下一轮'.format(num))
        except Exception as e:
            do_log.info('第{}轮测试 Fail,获取错误信息'.format(num))
            adb.screencap(picture_path,module=num)
        # 开始重启设备
        adb.power_reboot()
        do_log.info("设备正在重启,请稍候...")
        time.sleep(20)
        while True:
            time.sleep(1)
            result, window = adb.windows("Window")
            if result:
                break

        # 断言一：30秒内检测launcher是否启动
        do_log.info("断言一：30秒内检测launcher是否启动")
        count = 0
        while True:
            self.result, window = adb.windows("launcher")
            time.sleep(1)
            if self.result:
                do_log.info("开机成功")
                break
            if count == 30:
                do_log.info("未检测到TV进入桌面launcher，本次开机失败")
                # 获得当前时间
                now = datetime.datetime.now()
                # 转换为指定的格式:
                debug_time = now.strftime("%Y-%m-%d %H:%M:%S")
                do_log.info("launcher启动异常，第" + str(num) + "轮 reboot 测试fail")
                do_log.info("研发debug时间戳:" + str(debug_time))
                assert 1 == 2, "重启失败"
            count = count + 1

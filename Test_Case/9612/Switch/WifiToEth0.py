# -*- coding: utf-8 -*-
'''有线切wifi测试'''
import pytest,time,os

class Test_WifiToEth0():
    @pytest.mark.parametrize('num', range(1,100000))
    # @pytest.mark.usefixtures('setup_adb_device')
    def test_WifiToEth0(self,num,init_data):
        do_log,adb,picture_path,error_path,record_path,tombstones_path,anr_path,do_logcat = init_data
        do_log.info("第 {} 轮测试开始".format(num))
        adb.back(1, 3)
        if num ==1:
            do_logcat.open("test")
        #打开eth0
        do_log.info("关闭有线开关")
        adb.order("ifconfig eth0 down",time_out=10)
        time.sleep(5)
        wifi_pin = wifi_ping(adb, num, picture_path,retry=10)
        do_log.info("打开有线开关")
        adb.order("ifconfig eth0 up",time_out=10)
        time.sleep(5)
        eth0_pin = wifi_ping(adb, num, picture_path,retry=10)
        try:
            assert wifi_pin,"eth0关闭时，wifi回连失败"
            assert eth0_pin,"eth0打开时，有线网络断联"
        except Exception as e:
            do_log.info("错误类型：{}".format(e))
        do_log.info("进入下一轮")

def wifi_ping(adb, num, picturepath,retry=1):
    for i in range(retry):
        time.sleep(1)
        network = adb.order("ping -c 3 www.baidu.com",time_out=10)
        if "ttl" in network:
            print("第 " + str(num) + " 轮测试网络ping成功")
            return True
        if i ==(retry-1):
            adb.back(1,3)
            adb.menu_longpress()
            adb.ok()
            print('wifi图标显示异常，第 ' + str(num) + ' 轮ping网络失败')
            # 获取异常连接图片
            pt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            name1 = '第' + str(num) + "轮_" + str(pt) + 'ping网络失败.png'
            name = os.path.join(picturepath, name1)
            adb.screencap(name,type=0)
            time.sleep(3)
            return False
        print("回连超时，尝试retry")


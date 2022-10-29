# -*- coding: utf-8 -*-
'''有线切wifi测试'''
import pytest,time,os

class Test_AiyiqiToBili():
    @pytest.mark.parametrize('num', range(1,100000))
    # @pytest.mark.usefixtures('setup_adb_device')
    def test_AiyiqiToBili(self,num,init_driver,init_data):
        driver = init_driver
        do_log,adb,picture_path,error_path,record_path,tombstones_path,anr_path,do_logcat = init_data
        do_log.info("第 {} 轮测试开始".format(num))
        adb.back(1, 3)
        if num ==1:
            do_logcat.open("test")
        try:
            #统一标志位Launcher
            adb.order("monkey -p com.heytap.tv.launcher 1",time_out=10)
            do_log.info("播放云视听小电视")
            #播放云视听小电视
            Bili_movie(adb,num,2)
        except Exception as e:
            do_log.info("未知异常，进入下一轮：{}".format(e))

def Aiyiqi(adb):
    adb.app_stop(package="com.gitvvideo.oppo")
    adb.app_start(package="com.gitvvideo.oppo/com.gala.video.app.epg.ui.search.QSearchActivity")
    time.sleep(5)
    #搜索片源“沐浴之王”
    adb.left(2,2)
    adb.ok(1, 2)
    adb.down(2, 2)
    adb.ok(1, 2)
    adb.right(1, 2)
    adb.ok(1, 2)
    adb.up(1, 2)
    adb.right(3,2)
    adb.ok(1, 2)
    adb.right(3,2)
    adb.ok(1, 5)
    adb.left(1, 2)
    adb.ok(1, 2)
    time.sleep(60) #播放30秒
    adb.home(1, 2)

def Bili_movie(adb,num,playtime):
    if num==1:
        adb.app_stop(package="com.xiaodianshi.tv.yst")
    adb.app_start(package="com.xiaodianshi.tv.yst/com.xiaodianshi.tv.yst.ui.main.MainActivity")
    time.sleep(5)
    adb.ok(1,2)
    adb.left(1, 2)
    adb.down(1, 2)
    adb.ok(1, 2)
    count =1
    while True:
        for i in range(playtime):
            time.sleep(300)
        print("切换轮次记录：{}".format(count))
        adb.down(1,2)
        result, win = adb.windows("com.xiaodianshi.tv.yst.ui.main.MainActivity")
        if not result:
            adb.app_stop(package="com.xiaodianshi.tv.yst")
            break
        count=count+1

# def Bili(adb,num):
#     if num==1:
#         adb.app_stop(package="com.xiaodianshi.tv.yst")
#     adb.app_start(package="com.xiaodianshi.tv.yst/com.xiaodianshi.tv.yst.ui.main.MainActivity")
#     time.sleep(5)
#     #搜索片源“夺冠”
#     adb.ok(1,2)
#     adb.down(1,2)
#     adb.up(2,2)
#     adb.ok(1, 2)
#     adb.up(2, 2)
#     adb.ok(1, 2)
#     adb.down(1, 2)
#     adb.left(3, 2)
#     adb.ok(1, 2)
#     adb.right(9, 2)
#     adb.ok(2, 2)
#     time.sleep(5)  # 播放30秒"夺冠"
#     adb.home(1, 2)

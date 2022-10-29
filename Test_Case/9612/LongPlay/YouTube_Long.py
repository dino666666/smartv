# -*- coding: utf-8 -*-
'''youtube 4K片源长稳播放，需要登录账号'''
import pytest,time

from Common.Globe_Lib.Adbevent import ADB
from Common.Globe_Lib.maneger_devices_info import ManageDevices
from Common.Globe_Api.App_Playcontrol import App_Playcontrol

class Test_YouTube_LT():
    @pytest.mark.parametrize('num', range(1,100000))
    # @pytest.mark.usefixtures('setup_adb_device')
    def test_YouTube_LT(self,num,init_data):
        do_log,adb,picture_path,error_path,record_path,tombstones_path,anr_path,do_logcat = init_data
        global time_start,result
        if num ==1:
            time_start = time.time()
            do_logcat.open("test")
        time.sleep(1)
        time_end = time.time()
        time_c= round(time_end - time_start)
        long_time = 40   #压测时长 单位：分钟
        try:
            do_log.info("检查当前Activity")
            result, win = adb.windows("youtube")
        except Exception as e:
            do_log.info("argument of type 'NoneType' is not iterable:{}".format(e))
        if (not result) or (time_c >long_time*60):
            time_start = time.time()
            do_log.info("不在播放状态，重新播放")
            adb.order("monkey -p com.google.android.tvlauncher 1")
            d = App_Playcontrol(adb, 1)
            d.start()
            d.into_play_4K()
        do_log.info("播放状态正常,继续监控...")






# if __name__ == '__main__':
#
#     device = ManageDevices().get_devices()[0]
#     adb = ADB(device)
#     time_start = time.time()
#     while True:
#         result=""
#         time.sleep(1)
#         time_end = time.time()
#         time_c= round(time_end - time_start)
#         long_time = 40   #压测时长 单位：分钟
#         try:
#             result, win = adb.windows("youtube")
#         except Exception as e:
#             print("argument of type 'NoneType' is not iterable:{}".format(e))
#         if (not result) or (time_c >long_time*60):
#             time_start = time.time()
#             print("不在播放状态，重新播放")
#             adb.order("monkey -p com.google.android.tvlauncher 1")
#             d = App_Playcontrol(adb, 1)
#             d.start()
#             d.into_play_4K()
#         print("播放状态正常")

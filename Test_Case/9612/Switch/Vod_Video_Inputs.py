# -*- coding: utf-8 -*-

import pytest

from Common.Globe_Api.App_Playcontrol import App_Playcontrol
from Common.Globe_Api.Setting_Page import Setting

class Test_Switch():
    @pytest.mark.parametrize('num', range(1,100000))
    # @pytest.mark.usefixtures('setup_adb_device')
    def test_switch(self,num,init_data):
        do_log,adb,picture_path,error_path,record_path,tombstones_path,anr_path,do_logcat = init_data
        do_log.info("第 {} 轮测试开始".format(num))
        if num ==1:
            do_logcat.open("test")
        #统一标志位
        adb.app_start("com.google.android.tvlauncher/com.google.android.tvlauncher.MainActivity")
        try:
            # 用例执行
            do_log.info("YouTube")
            App_Playcontrol(adb,1).test_play()
            do_log.info("本地播放")
            Setting(adb).inputs_switch(7)
            App_Playcontrol(adb,5).into_play()
            do_log.info("HDMI通道")
            Setting(adb).hdmi1_hdmi3()
        except Exception as e:
            do_log.info("未知异常：{}".format(e))
        adb.pull('/data/anr', anr_path)
        adb.pull('/data/tombstones', tombstones_path)
        # #断言:是否投屏成功
        # try:
        #     assert result,"视频播放异常"
        #     do_log.info("视频正常播放，下一轮")
        # except Exception as e:
        #     do_log.info("开机失败{}".format(e))




# -*- coding: utf-8 -*-

import pytest,time

from Common.Globe_Api import Monkey_Page
from Common.Globe_Lib.myConfig import myConfig
from Common.Globe_Path import real_path

class Test_Monkey():
    # @pytest.mark.parametrize('num', range(1, 100000))
    # @pytest.mark.usefixtures('setup_adb_device')
    def test_monkey(self, init_data):
        do_log, adb, picture_path, error_path, record_path, tombstones_path, anr_path, do_logcat = init_data
        d = Monkey_Page.monkey_page(driver="driver", adb=adb, do_log=do_log,do_logcat=do_logcat)

        cf = myConfig(real_path.caseconfig_file)
        test_app = cf.getConfig("App","test_app")
        # 1.monkey初始化
        d.init_date(test_app)
        # 3.断言
        #两次monkey.log的文件大小一样才结束
        while True:
            do_log.info("读取monkey.log文件大小")
            value = d.assert_monkey(retry=10)
            if value:
                do_log.info("测试结束")
                break
            else:
                time.sleep(1)
                do_log.info("Monkey程序正在运行中...")
        do_log.info("开始拷贝测试数据")
        logcat_file = d.copy_log(error_path)










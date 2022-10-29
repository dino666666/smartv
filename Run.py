# -*- coding: utf-8 -*-

import pytest,configparser,multiprocessing

from concurrent.futures import ThreadPoolExecutor, as_completed
from Common.Globe_Lib.maneger_devices_pool import devices_pool
from Common.Globe_Lib.maneger_appium_server import ManageAppiumServer

from Common.Globe_Tools.function import *
from Common.Globe_Path import real_path
from Common.Globe_Lib.myConfig import myConfig

def run_case(device):
    config = configparser.ConfigParser()
    #读取用例配置文件
    config.read(real_path.caseconfig_file,encoding='utf-8')
    #获取用例
    test_case_dir = config.get("Case","case_dir")
    project_id = config.get("Case","project_id")
    case_file = config.get("Case","case_file")
    testcase =  os.path.join(real_path.test_case_base_dir,project_id,test_case_dir,case_file)
    print("读取到用例：{}".format(testcase))
    #执行器
    pytest.main(["-s","-v",testcase,
                 "--cmdopt={}".format(device),
                 "--html={}".format(real_path.report_file),"--self-contained-html"]
                )

if __name__ == '__main__':
    # multiprocessing.freeze_support()
    # tools_id = eval(myConfig(real_path.caseconfig_file).getConfig("Tool","tools_id"))
    a = myConfig(real_path.caseconfig_file)
    # print("real_path.caseconfig_file:{}".format(real_path.caseconfig_file))
    tools_id = eval(a.getConfig("Tool", "tools_id"))
    # print("检查操作系统")
    platform_name, appium_server_path = Check_system()
    # print("新建日志文件夹")
    init_logdir()
    # print("读取测试设备")

    '''根据tools_id启动对应的测试工具：Appium or Uiautomator2 or Adb'''
    if tools_id==1:
        devices_appium = devices_pool(type=1)
        print("启动Appium服务")
        # 获取资源池中的appium参数表
        if devices_appium and platform_name and appium_server_path:
            #创建线程池
            T =ThreadPoolExecutor()
            #实例化appium服务管理类
            mas = ManageAppiumServer(appium_server_path)
            #根据设备池设备数量启动相应的服务个数
            for dev in devices_appium:
                #检查appium服务是否被占用
                mas.stop_appium(platform_name,dev["port"])
                #启动appium服务
                task = T.submit(mas.start_appium_server,dev["port"])
                time.sleep(1)
            '''【建立多线程库obj_list，多线程执行测试用例】'''
            time.sleep(15)
            obj_list = []
            for dev in devices_appium:
                index =devices_appium.index(dev)
                task = T.submit(run_case,dev)
                obj_list.append(task)
                time.sleep(6)

            #等待测试用例执行完成
            for future in as_completed(obj_list):
                data =future.result()

            #杀掉appium服务，释放端口
            for dev in devices_appium:
                mas.stop_appium(platform_name,dev["port"])
                time.sleep(2)

    elif tools_id==2:
        devices_appium = devices_pool(type=0)
        print("启动uiautomator2服务或adb单进程服务")
        devices_num = []
        devices_list = []
        device_dict = []
        # print("获取到的设备列表：{}".format(devices_appium))
        #遍历设备列表
        for dev in devices_appium:
            devices_list.append(dev['caps']['deviceName'])

        if devices_list:
            for i in range(1,1+len(devices_list)):
                devices_num.append(i)
            device_dict = {i:devices_list[devices_num.index(i)] for i in devices_num}
        print("获取到的设备列表：{}".format(device_dict))
        select = input("请输入设备前面的序号，按enter键继续：")
        deviceid = devices_appium[eval(select)-1]
        run_case(deviceid)

    elif tools_id==3:
        devices_appium = devices_pool(type=1)
        print("启动adb多进程服务")
        if devices_appium and platform_name and appium_server_path:
            #创建线程池
            T =ThreadPoolExecutor()
            for dev in devices_appium:
                time.sleep(1)

            obj_list = []
            for dev in devices_appium:
                index =devices_appium.index(dev)
                task = T.submit(run_case,dev)
                obj_list.append(task)
                time.sleep(6)

            #等待测试用例执行完成
            for future in as_completed(obj_list):
                data =future.result()
# -*- coding: utf-8 -*-

import pytest,os,time,threading

from appium import webdriver
from Common.Globe_Lib.Adbevent import ADB
from Common.Globe_Lib.My_Logger import My_Log
from Common.Globe_Lib.Logcat import Logcat
from selenium import webdriver
from Common.Globe_Tools.function import *
from Common.Globe_Lib.maneger_devices_pool import devices_list

_lock = threading.Lock()

'''===========================【跨文件参数cmdopt】==========================='''
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--cmdopt")

'''===========================【初始化driver】==========================='''
#与appium建立连接，启动与appium的会话
def start_appium_session(device_info,server_params=None):
    if server_params is not None:
        device_info["caps"].update(server_params)
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(device_info["port"]),device_info["caps"])
    print('启动与设备 {} 会话成功！appium server端口为: {} '.format(device_info["caps"]["deviceName"],device_info["port"]))
    return driver

@pytest.fixture(scope="class")
def init_driver(setup_adb_device):
    adb,list_device,device,device_info = setup_adb_device
    try:
        print("服务启动中")
        driver = start_appium_session(device_info)
    except Exception as e:
        print("driver:adb not found!")
        # raise RuntimeError("driver:adb not found!")
        driver = 1
    adb.home()
    yield driver
    adb.inputs()
    try:
        driver.quit()
    except Exception as e:
        print('退出driver出现错误，为{}'.format(e))

@pytest.fixture(scope="function")
def setup_wifi_dc(setup_adb_device):
    '''wifi_dc专用'''
    adb,list_device,device,device_info = setup_adb_device
    # 开机
    while True:
        time.sleep(1)
        result,win=adb.windows('Window')
        if result:
            break
    sleep_min,sleep_max = devices_sorted(device)
    time.sleep(3)
    print('拉起driver休眠时间{}'.format(int(sleep_min) * 6))
    time.sleep(int(sleep_min) * 6)
    if Check_ADB(device):
        try:
            # with _lock:
            driver = start_appium_session(device_info)
        except Exception as e:
            print('{}拉起driver出现错误，为{}'.format(device, e))
            driver = 1
    else:
        print("driver:adb not found!{}".format(device))
        driver = 1
    adb.home()
    yield driver
    if driver != 1:
        adb.inputs()
        try:
            # with _lock:
            driver.quit()
        except Exception as e:
            print('{}退出driver出现错误，为{}'.format(device["caps"]["deviceName"], e))
    print('退出driver休眠时间{}'.format(int(sleep_max) * 6))
    time.sleep(int(sleep_max) * 6)
    adb.power_off()
    time.sleep(5)

'''===========================【初始化adb】==========================='''
@pytest.fixture(scope="class")
def setup_adb_device(cmdopt):
    '''获取adb，device，设备列表'''
    #从配置中读取log目录
    dir_name = get_logdir()
    test_log_dir = os.path.join(real_path.test_log_base_dir,dir_name)
    device_info = cmdopt
    device_info = eval(device_info)
    device = device_info['caps']['deviceName']
    adb = ADB(device)
    test_logdir_device = init_logdir_device(test_log_dir,device)
    list_device = logdata_dir(test_logdir_device)
    yield adb,list_device,device,device_info

'''===========================【初始化ALL】==========================='''
@pytest.fixture(scope="class")
def init_data(setup_adb_device):
    '''实例化和初始化日志工具和路径'''
    '''【logcat：0】【error：1】【picture：2】【record：3】【tombstones：4】【anr：5】【loggings：6】'''
    adb,list_device,device,device_info = setup_adb_device
    platform_name,appium_server_path = Check_system()
    do_log_path = os.path.join(list_device[6],Now(1)+'.log')
    do_log =My_Log(do_log_path)
    picture_path = list_device[2]
    error_path = list_device[1]
    record_path = list_device[3]
    tombstones_path = list_device[4]
    anr_path = list_device[5]
    do_logcat = Logcat(device,list_device[0],platform_name)
    yield do_log,adb,picture_path,error_path,record_path,tombstones_path,anr_path,do_logcat,device
    pass

def devices_sorted(device):
    devices_list_path = []
    for i in devices_list.devices_list:
        devices_list_path.append(i['deviceName'])
    new_devices_list_path = sorted(devices_list_path)
    print('设备文件地址排序为{}'.format(new_devices_list_path))
    for judge in range(len(new_devices_list_path)):
        if device == new_devices_list_path[judge]:
            print('{}文件地址为{}'.format(device, judge))
            break
    max_judge = (len(devices_list.devices_list) - 1) - judge
    return judge, max_judge

if __name__ == '__main__':
    file ='D:\\2_Logs\\1.png'
    # error_picture(file)



















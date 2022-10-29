# -*- coding: utf-8 -*-

import subprocess,time,chardet,os
import platform

from Common.Globe_Path import real_path
from Common.Globe_Lib.myConfig import myConfig

def subprocess_retry(command, time_out=3):
    '''
        防止管道阻塞
    :param command:
    :param time_out:
    :return:
    '''
    result = ""
    for i in range(3):
        p = subprocess.Popen(command, bufsize=10000,stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True, close_fds=True)
        try:
            if time_out:
                stdout, stderr = p.communicate(timeout=time_out)
                if stdout:
                    encoding = chardet.detect(stdout)["encoding"]
                    result = stdout.decode(encoding)
                    result = result.strip("\r\n")
                return result
            elif time_out==None:
                p.wait()
        except Exception as e:
            # logging.warning("{}".format(e))
            if p.poll() == None:
                # print(p.poll())
                p.kill()
                time.sleep(1)
            if p.stdin:
                p.stdin.close()
            if p.stderr:
                p.stderr.close()

# def subprocess_retry(command, time_out=3):
#     '''
#         防止管道阻塞
#     :param command:
#     :param time_out:
#     :return:
#     '''
#     result = ""
#     for i in range(3):
#         p = subprocess.Popen(command, bufsize=10000,stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True, close_fds=True)
#         try:
#             stdout, stderr = p.communicate(timeout=time_out)
#             if stdout and time_out:
#                 encoding =chardet.detect(stdout)["encoding"]
#                 result =stdout.decode(encoding)
#                 result = result.strip("\r\n")
#             return result
#         except Exception as e:
#             # logging.warning("{}".format(e))
#             if p.poll() == None:
#                 print(p.poll())
#                 p.kill()
#                 time.sleep(1)
#             if p.stdin:
#                 p.stdin.close()
#             if p.stdout:
#                 p.stdout.close()
#             if p.stderr:
#                 p.stderr.close()

def Check_system():
    '''自动识别操作系统'''
    platform_name = ""
    appium_server_path = ""
    plat = platform.platform()
    if plat.find("Windows")!=-1:
        platform_name ="windows"
        appium_server_path = r'D:\Users\W9007445\AppData\Roaming\npm\node_modules\appium\build\lib\main.js'
    elif plat.find("Linux") != -1:
        platform_name = "linux"
        appium_server_path = '/opt/node-v10.10.0-linux-x64/lib/node_modules/appium/build/lib/main.js'
    return platform_name,appium_server_path

def Now(format=0):
    '''当前时间格式化，如：2021-02-19_15-04-04'''
    now = ''
    if format==0:
        now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
    else:
        now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return now

'''==========================【以下四个函数新建日志文件夹】==========================='''
def init_logdir_device(path,device):
    # 定义Test_Log文件夹下，设备的log文件，以device命名
    init_logdir_templete = path
    test_logdir_device = os.path.join(init_logdir_templete,device)
    if not os.path.exists(test_logdir_device):
        os.mkdir(test_logdir_device)
    return test_logdir_device
def logdata_dir(path):
    '''初始化logcat、error、picture、record、tombstones、anr、logging'''
    list_device = []
    list_datadir = ['logcat','error','picture','record','tombstones','anr','loggings']
    for data in list_datadir:
        datadir = os.path.join(path, data)
        if not os.path.exists(datadir):
            os.mkdir(datadir)
            list_device.append(datadir)
    return list_device
def init_logdir():
    #定义Test_Log新建文件夹的名字now
    now = Now()
    test_log_base_dir = real_path.test_log_base_dir
    test_log_dir = os.path.join(test_log_base_dir,now)
    if not os.path.exists(test_log_dir):
        os.mkdir(test_log_dir)
    d = myConfig(real_path.caseconfig_file)
    d.setConfig('LOGGING','log_file',now)

def get_logdir():
    d = myConfig(real_path.caseconfig_file)
    value = d.getConfig('LOGGING','log_file')
    return value


def Check_ADB(device):
    """
    是否连接上adb
    :param device: 设备序列号
    :return: 是否连接成功
    """
    for i in range(8):
        # print("check adb")
        command = 'adb devices'
        time.sleep(1)
        key = os.popen(command).read()
        if device in key:
            return True




if __name__ == '__main__':
    print(Now())
# -*- coding: utf-8 -*-

import yaml
import os

from Common.Globe_Path import real_path
from Common.Globe_Lib.maneger_devices_info import ManageDevices

class devices_list:
    devices_list=[]

def devices_pool(port=4723,system_port=8200,type=0):
    #读取yaml文件中的数据，即appium启动的固定参数
    dev_pool = []
    yaml_data = __get_yaml_data()
    #获取当前连接的所有设备，即appium启动的动态参数
    all_devices_info =ManageDevices(type).get_devices_info()
    devices_list.devices_list = all_devices_info
    #合并动态参数和固定参数
    if all_devices_info:
        for info in all_devices_info:
            info.update(yaml_data)
            info["systemPort"] =system_port
            new_dict ={"caps":info,"port":port}
            dev_pool.append(new_dict)
            port +=4
            system_port+=4
    return dev_pool



def __get_yaml_data():
    yaml_path =os.path.join(real_path.yaml_file)
    with open(yaml_path,encoding="utf-8") as f:
        desired_template = yaml.load(f,yaml.FullLoader)
        return desired_template

if __name__ == '__main__':
    devices = devices_pool()
    pass
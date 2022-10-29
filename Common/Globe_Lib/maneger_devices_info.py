# -*- coding: utf-8 -*-

import time
import chardet

from Common.Globe_Tools.function import subprocess_retry

class ManageDevices:
    def __init__(self,type=1):
        self.__devices_info=[]
        #重启adb服务
        if type==1:
            subprocess_retry("adb kill-server",time_out=5)
            time.sleep(1)
            subprocess_retry("adb start-server",time_out=5)

    def get_devices_info(self,*paichu):
        '''
        主要功能：获取已连接设备的uuid和版本号
        :return:所有已连接设备的uuid和版本号
        '''
        self._get_devices_id(*paichu)
        self._get_device_platform_version()
        self._get_udid()
        return self.__devices_info

    def _get_udid(self):
        if self.__devices_info:
            for i in self.__devices_info:
                i["udid"]=i["deviceName"]

    def _get_device_platform_version(self):
        '''
        获取已连接设备的安卓版本号
        :return:
        '''
        if self.__devices_info:
            for dev in self.__devices_info:
                command = "adb -P 5037 -s {} shell getprop ro.build.version.release".format(dev['deviceName'])
                dev["platformVersion"] = subprocess_retry(command)

    def _get_devices_id(self,*paichu):
        '''
        获取设备deviceid
        :param paichu:
        :return:列表，所有设备
        '''
        result = subprocess_retry("adb devices")
        device_list =result.split("\n")
        for item in device_list:  # 遍历adb devices 输出的内容
            if item.find("\t") != -1:  # 获取设备信息
                temp = item.split("\t")
                if temp[1] == "device" or temp[1] == "device\r":  # 设备为可识别状态。有些可能是offline、unauthorized等。
                    new_device = {"deviceName": temp[0]}
                    if paichu is None:
                        self.__devices_info.append(new_device)
                    else:
                        if temp[0] in paichu:
                            pass
                        else:
                            self.__devices_info.append(new_device)

    def get_devices(self):
        '''
        获取所有的设备device_id,暂不兼容无线adb
        :param
        :return:列表，所有设备
        '''
        devices=[]
        result = subprocess_retry("adb devices")
        device_list =result.split("\n")
        for item in device_list:  # 遍历adb devices 输出的内容
            if item.find("\t") != -1:  # 获取设备信息
                temp = item.split("\t")
                if temp[1] == "device" or temp[1] == "device\r":  # 设备为可识别状态。有些可能是offline、unauthorized等。
                    devices.append(temp[0])
        return devices

if __name__ == '__main__':
    a = ManageDevices().get_devices()
    print(a)
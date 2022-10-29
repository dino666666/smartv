# -*- coding: utf-8 -*-
import time
import os

from Common.Globe_Lib.maneger_devices_info import ManageDevices
from Common.Globe_Path.locator_appium import USB_Play_Locator, Size_Window, WIFI_Locator, APP_Locator, HDMI_Locator, vedioplayer

class Setting():

    def __init__(self,adb):
        self.adb = adb

    def button_open(self):
        # Setting界面
        self.adb.order("input keyevent --longpress 136")

    def button_Network(self):
        #WIFI界面
        self.button_open()
        self.adb.ok(1,1)

    def hdmi1_hdmi3(self):
        list_inputs =[1,2,3]
        for inputs in list_inputs:
            self.inputs_switch(inputs)

    def inputs_switch(self,args):
        # HDMI1
        if args==1:
            self.adb.inputs()
            print("进入HDMI1通道")
            self.adb.ok(1,2)
            time.sleep(20)
        # HDMI2
        elif args==2:
            self.adb.inputs()
            self.adb.down(1, 2)
            print("进入HDMI2通道")
            self.adb.ok(1, 2)
            time.sleep(20)
        # HDMI3
        elif args == 3:
            self.adb.inputs()
            self.adb.down(2, 2)
            print("进入HDMI3通道")
            self.adb.ok(1, 2)
            time.sleep(20)
        # AV
        elif args == 4:
            self.adb.inputs()
            self.adb.down(3, 2)
            print("进入AV通道")
            self.adb.ok(1, 2)
            time.sleep(20)
        # ATV
        elif args == 5:
            self.adb.inputs()
            self.adb.down(4, 2)
            print("进入ATV通道")
            self.adb.ok(1, 2)
            time.sleep(20)
        # DTV
        elif args == 6:
            self.adb.inputs()
            self.adb.down(5, 2)
            print("进入DTV通道")
            self.adb.ok(1, 2)
            time.sleep(20)
        # USB
        elif args == 7:
            self.adb.inputs()
            self.adb.down(6, 2)
            print("进入USB通道")
            self.adb.ok(1, 2)
            time.sleep(20)




if __name__ == '__main__':

    device = ManageDevices().get_devices()[0]
    d = Setting(device)
    d.inputs_switch(7)

# -*- coding: utf-8 -*-

import os,subprocess,time,logging

from Common.Globe_Tools.function import *
from Common.Globe_Lib.My_Logger import My_Log
# logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(threadName)s - %(message)s')

do_log = My_Log()

class ADB(object):
    def __init__(self,device):
        self.device = device

    def cycle(self,num,times,commond):
        '''命令延时和次数定义'''
        for i in range(num):
            do_log.info(commond)
            subprocess_retry(commond)
            time.sleep(times)
            # devices= subprocess_retry("adb devices")
            # if self.device not in devices:
            #     do_log.info("adb:adb not found!")
            #     pass

    def windows(self,keyword):
        '''查看当前包名'''
        command = 'adb -s '+self.device+ ' shell "dumpsys window |grep mCurrentFocus"'
        key = subprocess_retry(command,time_out=5)
        if keyword in  key:
            return True,key
        else:
            return False,key

    def ok(self,num=1,times=0):
        '''【ok】键值'''
        ok = 'adb -s ' + self.device + ' shell input keyevent 23'
        self.cycle(num,times,ok)

    def back(self,num=1,times=0):
        '''【返回】键值'''
        back='adb -s '+self.device+' shell input keyevent 4'
        self.cycle(num,times,back)

    def left(self,num=1,times=0):
        '''【向左】键值'''
        ok = 'adb -s ' + self.device + ' shell input keyevent 21'
        self.cycle(num,times,ok)

    def right(self,num=1,times=0):
        '''【向右】键值'''
        ok = 'adb -s ' + self.device + ' shell input keyevent 22'
        self.cycle(num,times,ok)

    def down(self,num=1,times=0):
        '''【向右】键值'''
        down = 'adb -s ' + self.device + ' shell input keyevent 20'
        self.cycle(num,times,down)

    def menu_longpress(self):
        '''【长按menu弹出setting菜单】键值'''
        subprocess_retry('adb -s ' + self.device + ' shell input keyevent --longpress 82')

    def up(self,num=1,times=0):
        '''【向右】键值'''
        up = 'adb -s ' + self.device + ' shell input keyevent 19'
        self.cycle(num,times,up)

    def power_reboot(self):
        '''【长按power选择重启】键值'''
        subprocess_retry('adb -s ' + self.device + ' shell input keyevent --longpress F2')
        time.sleep(1)
        subprocess_retry('adb -s ' + self.device + ' shell input keyevent 22')
        time.sleep(1)
        subprocess_retry('adb -s ' + self.device + ' shell input keyevent 23')
        time.sleep(1)

    def power_sleep(self):
        '''【长按power选择重启】键值（国内外有差异）'''
        subprocess_retry('adb -s ' + self.device + ' shell input keyevent --longpress F2')
        time.sleep(1)
        subprocess_retry('adb -s ' + self.device + ' shell input keyevent 23')
        time.sleep(1)

    def power_off(self):
        '''【长按power选择关机】键值（国内外有差异）'''
        subprocess_retry('adb -s ' + self.device + ' shell input keyevent --longpress F2')
        time.sleep(1)
        subprocess_retry('adb -s ' + self.device + ' shell input keyevent 23')
        time.sleep(1)

    def voice_jia(self,num=1,times=0,type=0):
        '''【音量+】键值'''
        if type==0:
            down = 'adb -s ' + self.device + ' shell input keyevent 24'
            self.cycle(num,times,down)
        else:
            down = 'adb -s ' + self.device + ' shell input keyevent --longpress 24'
            self.cycle(num,times,down)

    def voice_jian(self,num=1,times=0,type=0):
        '''【音量-】键值'''
        if type==0:
            down = 'adb -s ' + self.device + ' shell input keyevent 25'
            self.cycle(num,times,down)
        else:
            down = 'adb -s ' + self.device + ' shell input keyevent --longpress 24'
            self.cycle(num,times,down)

    def order(self,command,type=0,time_out=2):
        '''【命令行】键值'''
        if type==0:
            command = 'adb -s '+self.device+' shell '+ command
            p = subprocess_retry(command,time_out)
            # do_log.info(command)
            return p
        else:
            command = 'adb -s ' + self.device + ' ' + command
            p = subprocess_retry(command,time_out)
            do_log.info(command)
            return p

    def inputs(self):
        '''【信源】键值'''
        inputs='adb -s '+self.device+' shell input keyevent 136'
        subprocess_retry(inputs)
        time.sleep(1)

    def home(self,num=1,times=0):
        '''【主页】键值'''
        home='adb -s '+self.device+' shell input keyevent 3'
        self.cycle(num,times,home)

    def pull(self,tv_path,pc_path):
        '''【adb pull TV PC】'''
        pull='adb -s '+self.device+' pull '+tv_path+' '+pc_path
        subprocess_retry(pull)
        do_log.info(pull)

    def push(self,pc_path,tv_path):
        '''【adb pull PC TV】'''
        push = 'adb -s '+self.device+' push '+pc_path+' '+tv_path
        subprocess_retry(push)
        do_log.info(push)

    def app_start(self,package=None,times=5,keyword='com'):
        start = 'adb -s '+self.device+' shell am start -W '+package
        subprocess_retry(start)
        time.sleep(times)
        command = 'adb -s ' + self.device + ' shell "dumpsys window | grep mCurrent"'
        key = subprocess_retry(command)
        if keyword in key:
            return True,key
        else:
            return False,key

    def app_stop(self,package=None,times=2,keyword='com'):
        stop='adb -s '+self.device+' shell am force-stop '+package
        subprocess_retry(stop,time_out=1)
        time.sleep(times)
        command = 'adb -s ' + self.device + ' shell "dumpsys window | grep mCurrent"'
        key = subprocess_retry(command)
        if keyword in key:
            return False, key
        else:
            return True, key

    def screencap(self,path=None,module=None,type=0):
        if type == 0:
            pt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            name1 = str(module) + str(pt) +'.png'
            name = os.path.join(path,name1)
            screencap='adb -s '+self.device+' shell screencap /sdcard/'+ name1
            pull = 'adb -s '+self.device+' pull /sdcard/'+ name1 +' '+path
            subprocess_retry(screencap,time_out=None)
            time.sleep(3)
            subprocess_retry(pull)
            time.sleep(1)
            # do_log.info(screencap)
            return name
        else:
            pt = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            name1 = str(module) + str(pt) +'.png'
            name = os.path.join(path,name1)
            screencap = 'adb -s ' + self.device + ' exec-out screencap -p > ' + name
            subprocess_retry(screencap)
            time.sleep(2)
            return name

if __name__ == '__main__':
    device = '00000A091A2009E01'
    adb = ADB(device)
    print(adb.order('ls -l /sdcard/'))




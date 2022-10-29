# -*- coding: utf-8 -*-

import time,logging,os,threading
from Common.Globe_Lib.Base_appium import Base
from Common.Globe_Tools.function import *

class monkey_page(Base):
    def init_date(self,app):
        self.adb.order("root",type=1)
        self.adb.order("rm -rf /data/anr/*")
        self.adb.order("rm -rf /data/tombstones/*")
        self.adb.order("killall logcat")
        self.adb.order("logcat -c")
        t1 = threading.Thread(target=logcat,args =(self.adb,))
        t2 = threading.Thread(target=monkey_run, args=[self.adb,app])
        t1.start()
        t2.start()
        time.sleep(5)

    def assert_monkey(self,retry=1):
        for i in range(retry):
            list_temp=[]
            for i in range(2):
                out = self.adb.order("ls -l /data/monkey.log",time_out = 20)
                output = out.split()[4]
                list_temp.append(output)
                time.sleep(300)
            print(list_temp)
            if list_temp[0]==list_temp[1] and (i+1)==retry:
                return True
        return False

    def copy_log(self,path):
        self.adb.order("killall logcat")
        self.adb.pull('/data/zh-logcat.log',path)
        self.adb.pull('/data/monkey.log', path)
        self.adb.pull('/data/anr', path)
        self.adb.pull('/data/tombstones', path)
        logcat_file = os.path.join(path,'zh-logcat.log')
        return logcat_file

    def search_log(self,file,controll_f=0,controll_b=3):
        list_temp = []
        with open(file,'r',encoding='utf-8') as f:
            while True:
                read_out = f.readline()
                if not read_out:
                    break
                list_temp.append(read_out)
                if len(list_temp)==10:
                    result, key= self.keyword(list_temp[-1])
                    if self.keyword(list_temp[-1]):
                        # controll_forward:控制关键字前的输出日志，数字：打印后几行
                        controll_forward = controll_f
                        # controll_backward:控制关键字后的输出日志，数字：打印后几行
                        controll_backward = controll_b
                    if controll_forward > 0:
                        for i in range(controll_forward):
                            logging.info(list_temp[i-(controll_forward + 1)])
                        controll_forward=0
                    if controll_backward > 0:
                        logging.info(list_temp[-1])
                        controll_backward = controll_backward - 1
                    del list_temp[0]


    def keyword(self,read_line):
        key1 = '10'
        key2 = '22'
        key3 ='33'
        list_key = [key1,key2,key3]
        for key in list_key:
            if key in read_line:
                logging.info('======================【发现关键字:'+ key +'】======================')
                return True,key
        return False


def logcat(adb):
    adb.order('"' + "logcat -v time >/data/zh-logcat.log" + '"',time_out=None)

def monkey_run(adb,app):
    cmd = '"'+"monkey -p  "+app+"  --throttle 500 -s 9001 --pct-motion 10 --pct-nav 20 --pct-majornav 30 --pct-syskeys 30 --pct-appswitch 10 --pct-touch 0 --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --ignore-crashes -v -v -v 100000>/data/monkey.log" +'"'
    adb.order(cmd,time_out=None)

if __name__ == '__main__':
    d = monkey_page('device','driver','adb','do_log','do_logcat')
    file = r'D:/3_Code/2_main_code_uiautomator/Test_Case_For_Verify/zh-logcat.log'
    d.search_log(file)
    pass
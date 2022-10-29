#_*_encoding:utf-8_*_

import time,subprocess,os
class Logcat(object):
    #实时获取日志
    def __init__(self,device,log_path, system='windows'):
        self.device=device
        self.log_path=log_path
        self.system = system

    def open(self,module):
        #开启日志抓取
        lt=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
        self.logcat_name = module+'-logcat-'+lt+'.log'
        self.logpath=os.path.join(self.log_path,self.logcat_name)
        op = open(self.logpath, 'a', encoding='utf-8', errors='ignore')
        command1 = 'adb ' + ' -s ' + self.device + ' logcat -c'
        command2 = 'adb -s ' + self.device + ' logcat -v time'
        subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
        self.log=subprocess.Popen(command2,stdout=op,stderr=subprocess.PIPE,shell=True,close_fds=True)
        #print(self.log.pid)
        if self.system == "windows":
            """获取开启logcat时的两个进程pid"""
            process = os.popen('tasklist | findstr adb.exe')
            pid_name = process.readline()
            self.pid_list = []
            while pid_name:
                time.sleep(1)
                # print(pid_name)
                a = pid_name.split('                     ')
                b = a[1]
                c = b.split(' ')
                for i in range(len(c)):
                    if len(c[i]) == 0:
                        pass
                    else:
                        d = i
                        break
                e = c[i]
                pid = int(e)
                # 获取最新的进程号

                self.pid_list.append(pid)
                pid_name = process.readline()
                self.new_pid_list = list(reversed(self.pid_list))
            # print('进程长度为{}'.format(len(self.new_pid_list)))
            #print(self.new_pid_list)
            self.new_pid1 = self.new_pid_list[0]
            self.new_pid2 = self.new_pid_list[1]
            return self.logpath

    def close(self, close_all=False):
        if self.system == "linux":
            #关闭日志抓取device
            process = os.popen('ps -ef | grep -i ' + self.device)
            pid_name = process.readline()
            while pid_name:
                time.sleep(1)
                #print(pid_name)
                for i in pid_name.split(' '):
                    try:
                        pid=int(i)
                        print(pid)
                        os.system('kill -9 %s'%pid)
                        break
                    except:
                        pass
                pid_name = process.readline()

            #print('logcat end')
            return self.logpath
        if self.system == "windows":
            if close_all:
                """如果选择结束全部adb.exe进程"""
                process = os.popen('tasklist | findstr adb.exe')
                pid_name = process.readline()
                while pid_name:
                    time.sleep(1)
                    a = pid_name.split('                     ')
                    print(a)
                    b=a[1]
                    c=b.split(' ')
                    for i in range(len(c)):
                        if len(c[i]) == 0:
                            pass
                        else:
                            # d=i
                            break
                    e=c[i]
                    pid = int(e)
                    os.system('taskkill -PID %s -F' % pid)
                    #print('进程{}关闭了'.format(pid))
                    pid_name = process.readline()
            else:
                os.system('taskkill -PID %s -F' % self.new_pid1)
                os.system('taskkill -PID %s -F' % self.new_pid2)
                #print('进程{}和{}关闭了'.format(self.new_pid1,self.new_pid2))
            #print('logcat end')
            return self.logpath

if __name__ == '__main__':
    devices = '00000A091A2009E03'
    # logcat_path = Constants.LOGS_DIR
    # logcat_path1 = os.path.join("device_00","logcat")
    logcat_path1 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs','device_03', 'logcat')
    do_logcat = Logcat(devices, logcat_path1, "windows")
    do_logcat.open('test')
    time.sleep(10)
    do_logcat.close(close_all=True)
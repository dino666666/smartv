# -*- coding: utf-8 -*-
import subprocess
import os
import time

from Common.Globe_Tools.function import subprocess_retry

class ManageAppiumServer:
    '''用来启动或关闭appium服务的类'''
    def __init__(self,appium_server_path):
        self.server_path =appium_server_path

    def start_appium_server(self,port):
        '''启动appium服务'''
        # appium_log_path =os.path.join(real_path.test_log_base_dir,"appium_server_{}.log".format(port))
        command ="node {0} -p {1} " \
                 "--session-override " \
                 "--local-timezone " \
                 "--log-timestamp & ".format(self.server_path,port)
        subprocess_retry(command,time_out=None)

    def stop_appium(self,system,post_num=4723):
        '''关闭appium服务'''
        if system=='windows':
            p = subprocess_retry('netstat -ano|findstr {post_num}')
            #'  TCP    0.0.0.0:4723           0.0.0.0:0              LISTENING       14296'
            p_template = p.split()
            if p_template and 'LISTENING' in p_template:
                appium_server_pid = int(p_template[-1])
                subprocess_retry("taskkill -PID {} -F".format(appium_server_pid),time_out=2.5)
                print("appium_server已关闭")
        elif system == 'ubantu':
            '''待兼容'''
            p = subprocess_retry(f'lsof -i tcp:{post_num}')
            p_template = p.split()
            if p_template and 'LISTENING' in p_template:
                appium_server_pid = p_template[-1]
                subprocess_retry("taskkill -PID {} -F".format(appium_server_pid),time_out=5)
                print("appium_server已关闭")

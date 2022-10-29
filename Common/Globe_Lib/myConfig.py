# -*- coding: utf-8 -*-

import pytest,configparser,codecs

class myConfig(object):
    def __init__(self,configfile_path):
        self.cf = configparser.ConfigParser()
        self.configfile_path = configfile_path

    def getConfig(self,dicta, dictb):
        self.cf.read(self.configfile_path, encoding='unicode_escape')
        # print("self.configfile_path：{}".format(self.configfile_path))
        value = self.cf.get(dicta, dictb)
        # print("返回value")
        return value

    def setConfig(self,dicta,dictb,dictc):
        self.cf.read(self.configfile_path, encoding='unicode_escape')
        self.cf.set(dicta, dictb,dictc)
        with open(self.configfile_path,'w') as file:
            self.cf.write(file)
        # print("config value write done")

if __name__ == '__main__':
    test_file ='D:\\3_Code\\1_main_code_appium\\Config\\logconfig.conf'
    d =myConfig(test_file)
    value = d.getConfig('LOGGING','logfile_dir')
    print(value)
    value = d.setConfig('LOGGING','logfile_dir','100')
    print(value)
    value = d.getConfig('LOGGING','logfile_dir')
    print(value)
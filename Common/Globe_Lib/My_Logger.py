# -*- coding: utf-8 -*-

import logging,os,time

class My_Log:

    def __init__(self,path=None):
        self.path = path

    def my_log(self,msg,level='INFO'):
        fh =''
        # 定义一个日志收集器 my_logger
        my_logger = logging.getLogger()

        # 设置收集级别
        my_logger.setLevel(level)

        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(threadName)s: %(message)s')

        # 创建一个输出渠道，并设置输出级别
        ch = logging.StreamHandler() # 输出到控制台
        ch.setLevel(level)
        ch.setFormatter(formatter)
        if self.path:
            fh = logging.FileHandler(self.path, encoding='utf-8')
            fh.setLevel(level)
            fh.setFormatter(formatter)
            my_logger.addHandler(fh)

        # 对接收集器和输出渠道
        my_logger.addHandler(ch)

        # 收集日志
        if level=='INFO':
            my_logger.info(msg)
        elif level=='DEBUG':
            my_logger.debug(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)
        else:
            pass

        # 关闭渠道，去重
        my_logger.removeHandler(ch)
        if self.path:
            my_logger.removeHandler(fh)

    def info(self,msg):
        self.my_log(msg,level='INFO')

    def debug(self,msg):
        self.my_log(msg,level='DEBUG')

    def warning(self,msg):
        self.my_log(msg,level='WARNING')

    def error(self,msg):
        self.my_log(msg,level='ERROR')

    def critical(self,msg):
        self.my_log(msg,level='critical')

if __name__ == '__main__':
    do_log= My_Log()
    do_log.info("123")
    do_log.info("455")
    do_log.info("123")
    do_log.info("123")

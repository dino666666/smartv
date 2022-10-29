# -*- coding: utf-8 -*-

import os,time,sys

#当前时间
now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) #获取当前时间
'''====================================【Path】===================================='''
#项目_绝对路径
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#用例_绝对路径
test_case_base_dir = os.path.join(project_path,"Test_Case")
#日志_绝对路径
test_log_base_dir = os.path.join(project_path,"Test_Log")
#测试报告_绝对路径
report_dir = os.path.join(project_path,"Report")
'''====================================【File】===================================='''
#用例配置文件_绝对路径
# print("project_path:{}".format(project_path))
caseconfig_file = os.path.join(project_path,"Common","Globe_Config","case_cfg.ini")
# print("caseconfig_file:{}".format(caseconfig_file))
log_file = os.path.join(project_path,now+'.log')
#脚本log配置文件_绝对路径
logconfig_file = os.path.join(project_path,"Common","Globe_Config","logconfig.conf")
#测试报告文件_绝对路径
report_file = os.path.join(project_path,"Report",now+'.html')
#yaml文件_绝对路径
yaml_file = os.path.join(project_path,"Common","Globe_Config",'desired_caps.yaml')
#test_source文件_绝对路径
test_video = os.path.join(project_path,"Test_Source",'test_video.MP4')


if __name__ == '__main__':
    print(sys.path)
    # print(caseconfig_file)



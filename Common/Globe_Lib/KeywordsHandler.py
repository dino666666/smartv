#!/usr/bin/python3
# re.split('\W+', 'runoob, runoob, runoob.')  ['runoob', 'runoob', 'runoob', '']

import re, time, os



class KeywordsHandler:

    def __init__(self):
        pass
        
    @staticmethod  
    def search(pattern, string):
        # re.search 扫描整个字符串并返回第一个成功的匹配
        # re.search(pattern, string, flags=0)
        pat = re.compile(pattern)
        result = re.search(pat, string)
        return result

    # re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
    # re.match(pattern, string, flags=0)
    @staticmethod
    def match(pattern, string):
        pat = re.compile(pattern)
        result = re.match(pat, string)
        return result
    
    @staticmethod
    def findall(pattern, string):
        # re.compile(pattern[, flags])
        # result1 = re.findall(r'\d+','runoob 123 google 456')
        pat = re.compile(pattern)
        result = re.findall(pat, string)
        return result
    
    @staticmethod
    def sub(Patten, repl, string):
        # Python 的re模块提供了re.sub用于替换字符串中的匹配项。count=0 替换所有
        # re.sub(pattern, repl, string, count=0, flags=0)
        pat = re.compile(pattern)
        result = re.sub(pat, repl, string)
        return result
        
    def writeToText(line_list):
        with open("monkeyResult.txt", "w") as f:           
            f.write(line)

    @staticmethod
    def monkey_log_analyzer(filePath):
        monkey_log_keyword = [b" crash ", b"FATAL ", b"ANR", b"NullPointerException", b"OutOfMemoryError", b"StackOverflowError", b"ClassNotFoundException", b"tombstone", b"Exception"]
        crash_line = []
        fatal_line = []
        anr_line = []
        nullPointerException_line = []
        outOfMemoryError_line = []
        stackOverflowError_line = []
        classNotFoundException_line = []
        tombstone_line = []
        exception_line = []
        
        total_line = []
        
        monkey_log_keyword_dict = {}
        for i in monkey_log_keyword:
            monkey_log_keyword_dict[i] = 0
            #print(monkey_log_keyword_dict)
        with open(filePath, "rb") as file:
            for line in file:
                if line.find(monkey_log_keyword[0]) >= 0:
                    monkey_log_keyword_dict[monkey_log_keyword[0]] += 1
                    #print(line)
                    crash_line.append(line)

                elif line.find(monkey_log_keyword[1]) >= 0:
                    monkey_log_keyword_dict[monkey_log_keyword[1]] += 1
                    #print(line)
                    fatal_line.append(line)

                elif line.find(monkey_log_keyword[2]) >= 0:
                    monkey_log_keyword_dict[monkey_log_keyword[2]] += 1
                    #print(line)
                    anr_line.append(line)

                elif line.find(monkey_log_keyword[3]) >= 0:
                    monkey_log_keyword_dict[monkey_log_keyword[3]] += 1
                    #print(line)
                    nullPointerException_line.append(line)

                elif line.find(monkey_log_keyword[4]) >= 0:
                    monkey_log_keyword_dict[monkey_log_keyword[4]] += 1
                    #print(line)
                    outOfMemoryError_line.append(line)

                elif line.find(monkey_log_keyword[5]) >= 0:
                    monkey_log_keyword_dict[monkey_log_keyword[5]] += 1
                    #print(line)
                    stackOverflowError_line.append(line)

                elif line.find(monkey_log_keyword[6]) >= 0:
                    monkey_log_keyword_dict[monkey_log_keyword[6]] += 1
                    #print(line)
                    classNotFoundException_line.append(line)

                elif line.find(monkey_log_keyword[7]) >= 0:
                    monkey_log_keyword_dict[monkey_log_keyword[7]] += 1
                    #print(line)
                    tombstone_line.append(line)

                elif line.find(monkey_log_keyword[8]) >= 0:
                    monkey_log_keyword_dict[monkey_log_keyword[8]] += 1
                    exception_line.append(line)
                    #print(line)
        print(monkey_log_keyword_dict)
        total_line.append(crash_line)
        total_line.append(fatal_line)
        total_line.append(anr_line)
        total_line.append(nullPointerException_line)
        total_line.append(outOfMemoryError_line)
        total_line.append(stackOverflowError_line)
        total_line.append(classNotFoundException_line)
        total_line.append(tombstone_line)
        total_line.append(exception_line)
        
        #print(nullPointerException_line)
        current_work_dir = os.path.dirname(__file__)       
        current_work_dir = os.path.join(current_work_dir, "monkeyResult.txt")
        print("开始写入分析结果monkeyResult.txt")
        with open(current_work_dir, "wb") as f: 
            for key , value in monkey_log_keyword_dict.items():
                f.write(key+" : ".encode("utf-8")+str(value).encode("utf-8"))
                f.write(b'\n')
            f.write(b'\n')
            time.sleep(0.5)
            for line_list in total_line:
                for line in line_list:
                    f.write(line)
                f.write(b'\n')
        print("分析结果写入成功！")

        print("分析结果保存路径：", current_work_dir)
        """
        return monkey_log_keyword, crash_line, fatal_line, anr_line, nullPointerException_line, \
        outOfMemoryError_line, stackOverflowError_line, classNotFoundException_line, tombstone_line, exception_line
        """
    @staticmethod
    def re_monkey_log_analyzer(filePath):
        monkey_log_keyword = [b" crash ", b"FATAL ", b"ANR", b"NullPointerException", b"OutOfMemoryError", b"StackOverflowError", b"ClassNotFoundException", b"tombstone", b"Exception"]
        monkey_log_keyword_complile = []
        for keyword in monkey_log_keyword:
           monkey_log_keyword_complile.append(re.compile(keyword))
        crash_line = []
        fatal_line = []
        anr_line = []
        nullPointerException_line = []
        outOfMemoryError_line = []
        stackOverflowError_line = []
        classNotFoundException_line = []
        tombstone_line = []
        exception_line = []
        
        total_line = []
        
        monkey_log_keyword_dict = {}
        for i in monkey_log_keyword:
            monkey_log_keyword_dict[i] = 0
            #print(monkey_log_keyword_dict)
        with open(filePath, "rb") as file:
            for line in file:
                if len(monkey_log_keyword_complile[0].findall(line, re.I)) > 0:
                    monkey_log_keyword_dict[monkey_log_keyword[0]] += 1
                    #print(line)
                    crash_line.append(line)

                elif len(monkey_log_keyword_complile[1].findall(line, re.I)) > 0:
                    monkey_log_keyword_dict[monkey_log_keyword[1]] += 1
                    #print(line)
                    fatal_line.append(line)

                elif len(monkey_log_keyword_complile[2].findall(line, re.I)) > 0:
                    monkey_log_keyword_dict[monkey_log_keyword[2]] += 1
                    #print(line)
                    anr_line.append(line)

                elif len(monkey_log_keyword_complile[3].findall(line, re.I)) > 0:
                    monkey_log_keyword_dict[monkey_log_keyword[3]] += 1
                    #print(line)
                    nullPointerException_line.append(line)

                elif len(monkey_log_keyword_complile[4].findall(line, re.I)) > 0:
                    monkey_log_keyword_dict[monkey_log_keyword[4]] += 1
                    #print(line)
                    outOfMemoryError_line.append(line)

                elif len(monkey_log_keyword_complile[5].findall(line, re.I)) > 0:
                    monkey_log_keyword_dict[monkey_log_keyword[5]] += 1
                    #print(line)
                    stackOverflowError_line.append(line)

                elif len(monkey_log_keyword_complile[6].findall(line, re.I)) > 0:
                    monkey_log_keyword_dict[monkey_log_keyword[6]] += 1
                    #print(line)
                    classNotFoundException_line.append(line)

                elif len(monkey_log_keyword_complile[7].findall(line, re.I)) > 0:
                    monkey_log_keyword_dict[monkey_log_keyword[7]] += 1
                    #print(line)
                    tombstone_line.append(line)

                elif len(monkey_log_keyword_complile[8].findall(line, re.I)) > 0:
                    monkey_log_keyword_dict[monkey_log_keyword[8]] += 1
                    exception_line.append(line)
                    #print(line)
        print(monkey_log_keyword_dict)
        total_line.append(crash_line)
        total_line.append(fatal_line)
        total_line.append(anr_line)
        total_line.append(nullPointerException_line)
        total_line.append(outOfMemoryError_line)
        total_line.append(stackOverflowError_line)
        total_line.append(classNotFoundException_line)
        total_line.append(tombstone_line)
        total_line.append(exception_line)
        
        #print(nullPointerException_line)
        current_work_dir = os.path.dirname(__file__)       
        current_work_dir = os.path.join(current_work_dir, "re_monkeyResult.txt")
        print("开始写入分析结果re_monkeyResult.txt")
        with open(current_work_dir, "wb") as f: 
            for key , value in monkey_log_keyword_dict.items():
                f.write(key+" : ".encode("utf-8")+str(value).encode("utf-8"))
                f.write(b'\n')
            f.write(b'\n')
            time.sleep(0.5)
            for line_list in total_line:
                for line in line_list:
                    f.write(line)
                f.write(b'\n')
        print("分析结果写入成功！")
        print("分析结果保存路径：", current_work_dir)               
        
        


if __name__ == "__main__":

    filePath = input("please input file path: ")
    KeywordsHandler.re_monkey_log_analyzer(filePath)
    
        
        
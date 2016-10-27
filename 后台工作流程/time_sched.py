#!/usr/bin/python3
# coding:utf-8

'''
Created on:
@author:
Email:
Version:
Description:
Help: http://www.pythontab.com/html/2013/pythonjichu_0119/146.html
'''

'''
定时任务实现
'''
import time, os, sched

schedule = sched.scheduler(time.time, time.sleep)

def perform_command(cmd, inc):
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    os.system(cmd)

def timming_exe(cmd, inc = 60):
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    schedule.run()

if __name__ == "__main__":

    print("show time afer 1 seconds:")
    timming_exe("echo %time%", 1)


'''
python日志功能的实现
http://www.tuicool.com/articles/IRzMFb7

软件开发中通过日志记录程序的运行情况是一个开发的好习惯，对于错误排查和系统运维都有很大的帮助。
python标准库自带的日志模块即可。
'''

'''
mysql数据库的封装
http://blog.csdn.net/u012935755/article/details/50178251
1。一个连接方法
2。增删改查4个方法

'''
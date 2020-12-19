#!/usr/bin/env python
# encoding: utf-8

"""
@author: clover
@file: TestAllRunner.py
@time: 2018/8/21 23:33
"""

import threading
from TestAllCass import *

def threads():
    threads = []    #创建线程数组
    threads.append(threading.Thread(target=test_login()))   #定义线程，添加线程到数组
    # threads.append(threading.Thread(target=demo2()))
    for th in threads:   #读取数组里的所有线程，并同时执行
        th.setDaemon(True)   #将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
        th.start()	     #开始线程活动
    th.join()            #把主线程挂起，等待上面的线程跑完了再运行




#!/usr/bin/python
# -*- coding: UTF-8 -*-
import serial
import time


#实例化串口号、波特率、等待时间
#timeout=None 永远等待，直到有数据传过来（阻塞）  
#timeout=0 不等待，收不到数据直接退出读取（非阻塞） 
ser=serial.Serial('COM2',19200,timeout=1)

#打印串口信息 
print("串口信息：",ser)

#判断串口是否打开
print("串口是否打开",ser.isOpen())

#打印输出消息到串口
ser.write(b"hello")

#关闭串口
ser.close()


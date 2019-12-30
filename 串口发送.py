#!/usr/bin/python
# -*- coding: UTF-8 -*-
import serial
import time
import configparser
import os


#在传递键值对数据时，会将键名 全部转化为小写
conf = configparser.ConfigParser()
if os.path.isfile("seting.ini"):
    conf.read("seting.ini")
    COM_No  = conf.get("Serial_settings", "COM_No")
    baud=int(conf.get("Serial_settings","baud"))
    timeout=int(conf.get("Serial_settings","timeout"))
    bytesize=int(conf.get("Serial_settings","bytesize"))
    stopbits=int(conf.get("Serial_settings","stopbits"))    
    parity={"None":serial.PARITY_NONE,"EVEN":serial.PARITY_EVEN,"ODD":serial.PARITY_ODD}
    parity=parity[conf.get("Serial_settings","parity")]
else:
    conf.add_section('Serial_settings')
    conf.set('Serial_settings', 'COM_No', 'COM1')
    conf.set('Serial_settings', "baud", '19200')
    conf.set('Serial_settings', 'timeout', '1')
    conf.set('Serial_settings', 'bytesize', '8')
    conf.set('Serial_settings', 'stopbits', '1')
    conf.set('Serial_settings', 'parity', 'None')
    conf.write(open('seting.ini', 'w'))


print('获取指定的section下的option', type(parity), parity)

# 实例化串口号、波特率、等待时间
ser=serial.Serial(port=COM_No,
                  baudrate=baud,
                  bytesize=bytesize,
                  parity=parity,
                  stopbits = stopbits,
                  timeout=timeout)



#打印串口信息 
print("串口信息：",ser)

#判断串口是否打开
print("串口是否打开",ser.isOpen())

#打印输出消息到串口
ser.write(b"hello")

#关闭串口
ser.close()


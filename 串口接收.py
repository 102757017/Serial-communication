#!/usr/bin/python
# -*- coding: UTF-8 -*-
import serial
import time

'''
#timeout=None 永远等待，直到有数据传过来（阻塞),timeout=0 不等待，收不到数据直接退出读取（非阻塞）
name:设备名字
port：读或者写端口
baudrate：波特率
bytesize：字节大小
parity：校验位，可设置为：serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD, serial.PARITY_MARK, serial.PARITY_SPACE
stopbits：停止位
writeTimeout：写超时
xonxoff：软件流控
rtscts：硬件流控
dsrdtr：硬件流控
interCharTimeout:字符间隔超时
'''
# 实例化串口号、波特率、等待时间
ser=serial.Serial('COM1',19200,timeout=1,xonxoff=0)

# 打印串口信息 
print("串口信息：",ser)

# 判断串口是否打开
print("串口是否打开",ser.isOpen())

while True:
    #inWaiting()：返回接收缓存中的字节数
    while ser.inWaiting()>0:
        n=ser.inWaiting()
        print("缓存内的字节数",n)
        
        #读取n个字节，不能用以下方法，应为有延迟，读取的n可能偏小
        buffer=ser.read(ser.inWaiting())
        print("读取到数据:",buffer.decode("GBK"))
        
        #读取1行，使用readline()时应该注意：打开串口时应该指定超时，否则如果串口没有收到新行，则会一直等待。如果没有超时，readline会报异常。
        #buffer=ser.readline()
        #print("读取到数据:",buffer.decode("GBK")) 

# 关闭串口 
ser.close()

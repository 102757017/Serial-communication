#!/usr/bin/python
# -*- coding: UTF-8 -*-


#无符号整数
a=b'\xFF\xFF'
data=""
for x in a:
    #十进制转换为二进制
    x=bin(x)
    #二进制转换为字符串，并且去掉前端的0b
    s=str(x).replace('0b','')
    #将2进制字符串拼接
    data=data+s

#2进制字符串转为10进制
data=int(data,2)
print(data,type(data))


#有符号整数
a=b'\xFF\xFF'
data=""
for x in a:
    #十进制转换为二进制
    x=bin(x)
    #二进制转换为字符串，并且去掉前端的0b
    s=str(x).replace('0b','')
    #将2进制字符串拼接
    data=data+s

#2进制字符串转为10进制
data=int(data[1:],2)
print(data,type(data))

print(-1)

#十进制转换为二进制
print("2进制到16进制",bin(171))

#2进制到16进制
print("2进制到16进制",hex(0b10101011))

#16进制到2进制
print("16进制到2进制",bin(0xab))

#2进制字符串转为10进制
print("2进制字符串转为10进制",int("10101011",2))


#10进制转为16进制
print("10进制转为16进制",hex(171))

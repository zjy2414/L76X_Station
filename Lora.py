# -*- coding:utf-8 -*-

import serial
import time

#Lora信通发送数据
def Send(message):
    ser=serial.Serial("/dev/ttyUSB0",9600,timeout=1)     #配置Lora通讯串口
    ser.write(message+"\r\n")
    # time.sleep(0.1)
    ser.close()

def Receive():
    ser=serial.Serial("/dev/ttyUSB1",9600,timeout=2)     #配置Arduino温度气压串口
    return str(ser.readline().decode())
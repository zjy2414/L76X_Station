# -*- coding:utf-8 -*-

import serial
import time

#Lora信通发送数据
def Send(message):
    ser=serial.Serial("/dev/ttyUSB0",9600,timeout=1)     #配置Lora通讯串口
    ser.write(message)
    time.sleep(0.5)
    ser.close()
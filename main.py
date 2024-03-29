# -*- coding:utf-8 -*-

import L76X
import time
import math
import Lora
import daemon

def Main():
    try:
        x=L76X.L76X()
        x.L76X_Set_Baudrate(9600)
        x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
        time.sleep(2)
        x.L76X_Set_Baudrate(115200)

        x.L76X_Send_Command(x.SET_POS_FIX_400MS);

        #Set output message
        x.L76X_Send_Command(x.SET_NMEA_OUTPUT);

        x.L76X_Exit_BackupMode();
        while(1):
           x.L76X_Gat_GNRMC()  

           if(x.Status == 1):
               print 'Already positioned'
           else:
               print 'No positioning'

        #    print ' Lat = %f'%x.Lat
           x.L76X_Baidu_Coordinates(x.Lat, x.Lon)

           try:
               x.Get_GNGGA()
               x.Get_TP()
               message = "*" + str(x.Lon_Baidu) + "," + str(x.Lat_Baidu) + "," + x._Status + ',' + x.Satellites + ',' + x.Elevation + ',' + x.Temperture + ',' + x.Pressure
               Lora.Send(message)
           except:
               print("error.")
               Lora.Send("Main ERROR!")
        #    time.sleep(0.5)
    except:
        #GPIO.cleanup()
        print "\nProgram end"
        exit()

with daemon.DaemonContext():
    Main()
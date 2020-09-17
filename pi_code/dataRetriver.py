"""
Project Name : Home Weather Station
Purpose : To get the values from UNO and log it
Created on : 17 Sep 2020
Created by : Sashwat K <sashwat0001@gmail.com>
Revision : 3
Last Updated by : Sashwat K <sashwat0001@gmail.com>
Last updated on : 18 Sep 2020
"""

import serial
import logging

ser = serial.Serial("/dev/ttyACM0",9600)

logging.basicConfig(filename="app.log", level=logging.DEBUG,format="[%(asctime)s, %(message)s]", datefmt="%d/%m/%Y, %H:%M:%S")

def convertSerialToList(string):
    li = list(string.split(","))
    return li

def dataLogging(inputData):
    logging.debug(inputData)

def main():
    while True:
        read_serial = ser.readline().strip().decode("utf-8")
        theDataList = convertSerialToList(read_serial)
        if len(theDataList) == 12:
            dataLogging(theDataList)

if __name__ == "__main__":
    main()
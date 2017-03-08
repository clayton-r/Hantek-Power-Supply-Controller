import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/cu.SLAB_USBtoUART',
    baudrate=9600,
)
#    parity=serial.PARITY_ODD,
#    stopbits=serial.STOPBITS_TWO,
#    bytesize=serial.EIGHTBITS
#)

print (ser.name)       # check which port was really used

ser.write(bytes('si2000\r')) # write a string
time.sleep(5)
ser.write(bytes('si1000\r'))


ser.write(bytes('su2000\r'))
time.sleep(1)
ser.close()             # close port
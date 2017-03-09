import time
import serial

Ch1_Potential = 1000        #voltage in mV
Ch1_Current = 1000          #amperage in mA

Ch2_Potential = 1000        #voltage in mV
Ch2_Current = 1000          #amperage in mA

Ch1VoltageCall = 'su'
Ch1AmpereageCall = 'si'

Ch2VoltageCall = 'sa'
Ch2AmpereageCall = 'sd'

Return = '\r'

Ch1VoltageSet = Ch1VoltageCall + str(Ch1_Potential) + str(Return)
Ch1AmperageSet = Ch1AmpereageCall + str(Ch1_Current) + str(Return)

Ch2VoltageSet = Ch2VoltageCall + str(Ch2_Potential) + str(Return)
Ch2AmperageSet = Ch2AmpereageCall + str(Ch2_Current) + str(Return)

print '\r'

print ('Ch1 Voltage Set To: ' + str(Ch1_Potential) + ' mV')
print ('Ch1 Amperage Set To: ' + str(Ch1_Current) + ' mV')

print ('Ch2 Voltage Set To: ' + str(Ch2_Potential) + ' mV')
print ('Ch2 Amperage Set To: ' + str(Ch2_Current) + ' mV')

print '\r'

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/cu.SLAB_USBtoUART',
    baudrate=9600,
)

print ('Port: ' + ser.name)       # check which port was really used

print '\r'

#give it some time between commands


ser.write(bytes(Ch1VoltageSet))
time.sleep(.01)
ser.write(bytes(Ch1AmperageSet))

time.sleep(.01)

ser.write(bytes(Ch2VoltageSet))
time.sleep(.01)
ser.write(bytes(Ch2AmperageSet))

time.sleep(.01)

# ser.write(bytes('ru'))
# time.sleep(.01)
# ru = ser.readline()
# if int(ru) == int(Ch1_Potential):
#     print ('On Ch1(V): Confirmed ' + str(Ch1_Potential) + ' mV')
# else:
#     print ('On Ch1(V): You are a dumbass')
#
# time.sleep(.01)
#
# ser.write(bytes('ri'))
# time.sleep(.01)
# ri = ser.readline()
# if int(ri) == int(Ch1_Current):
#     print ('On Ch1(A): Confirmed ' + str(Ch1_Current) + ' mA')
# else:
#     print ('On Ch1(A): You are a dumbass')
#
# time.sleep(.01)
#
# ser.write(bytes('rk'))
# time.sleep(.01)
# rk = ser.readline()
# if int(rk) == int(Ch2_Potential):
#     print ('On Ch2(V): Confirmed ' + str(Ch2_Potential) + ' mV')
# else:
#     print ('On Ch2(V): You are a dumbass')
#
# time.sleep(.01)
#
# ser.write(bytes('rq'))
# time.sleep(.01)
# rq = ser.readline()
# if int(rq) == int(Ch1_Potential):
#     print ('On Ch2(A): Confirmed ' + str(Ch2_Current) + ' mA')
# else:
#     print ('On Ch2(A): You are a dumbass')


time.sleep(.01)

ser.close()             # close port


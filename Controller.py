import time
import serial
from Utils import send_command, serial_ports

ports = serial_ports()
print(ports)

Ch1_Potential = '16420'       # voltage in mV
Ch1_Current = '49'         # amperage in mA

#all four racks
# .049 A, 16.42V


#just three racks
# 11.97V 0.116A 14 low light
#  12.55V 0.267A 40 mod light
#15V 1.8A 180 high light

Ch2_Potential = '0000'       # voltage in mV
Ch2_Current = '0000'         # amperage in mA

cycle = 1              # Number of Cycles
period = 60*60*12*2*5              # Length of cycle (in seconds)

#time.sleep(10000)      #time lights off to settle

for i in range(cycle):
    print('Cycle: ' + str(i+1))

    send_command(1, Ch1_Potential, Ch1_Current)  # voltage and amperage in mV & mA
    #send_command(2, Ch2_Potential, Ch2_Current)  # voltage and amperage in mV & mA

    time.sleep(period/2)
    # time.sleep(2)

    send_command(1, '0000', '0000')  # voltage and amperage in mV & mA
    #send_command(2, 000, 000)  # voltage and amperage in mV & mA

    time.sleep(period/2)
    # time.sleep(2)

    i += 1
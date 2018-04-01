import time
import serial
from Utils import send_command, confirm_port

Ch1_Potential = '12000'       # voltage in mV
Ch1_Current = '0400'         # amperage in mA

Ch2_Potential = '12000'       # voltage in mV
Ch2_Current = '0400'         # amperage in mA

cycle = 10                  # Number of Cycles
period = 3600               # Length of cycle (in seconds)

for i in range(cycle):
    print('Cycle: ' + str(i+1))

    send_command(1, Ch1_Potential, Ch1_Current)  # voltage and amperage in mV & mA
    send_command(2, Ch2_Potential, Ch2_Current)  # voltage and amperage in mV & mA

    # time.sleep(period/2)
    time.sleep(1)

    send_command(1, 000, 000)  # voltage and amperage in mV & mA
    send_command(2, 000, 000)  # voltage and amperage in mV & mA

    # time.sleep(period/2)
    time.sleep(1)

    i += 1
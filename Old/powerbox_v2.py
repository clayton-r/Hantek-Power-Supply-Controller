import time
import serial

Ch1_Potential = '12000'       # voltage in mV
Ch1_Current = '0400'         # amperage in mA

Ch2_Potential = '2000'       # voltage in mV
Ch2_Current = '2000'         # amperage in mA

cycle = 10

period = 3600


def confirm_port():
    from check_ports import serial_ports

    result = serial_ports()

    if '/dev/tty.SLAB_USBtoUART' in result:
        print ('Power box connected on port:  /dev/tty.SLAB_USBtoUART')
        pass
    else:
        print('Power box not found.')
        exit()


def send_command(Channel, Potential, Current):

    channel = int(Channel)

    if channel == int(1):
        set_voltage = ('su' + str(Potential) + '\r').encode('ascii')
        set_current = ('si' + str(Current) + '\r').encode('ascii')
    elif channel == int(2):
        set_voltage = ('sa' + str(Potential) + '\r').encode('ascii')
        set_current = ('sd' + str(Current) + '\r').encode('ascii')
    else:
        print('Channel (int(1 or 2)) needs to be specified...')
        print (channel)
        exit()

    ser = serial.Serial(
        port='/dev/tty.SLAB_USBtoUART',
        baudrate=9600,
    )

    # print('the port acutally used is: Port: ' + ser.name)  # check which port was really used

    print('\r')

    ser.write(bytes(set_voltage))
    time.sleep(.1)
    ser.write(bytes(set_current))
    time.sleep(.1)


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

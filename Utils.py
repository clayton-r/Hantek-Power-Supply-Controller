import sys
import glob
import serial
import time


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def confirm_port():

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
        port='COM3',
        baudrate=9600,
    )

    # print('the port acutally used is: Port: ' + ser.name)  # check which port was really used

    print('\r')

    ser.write(bytes(set_voltage))
    time.sleep(.1)
    ser.write(bytes(set_current))
    time.sleep(.1)

import serial

class SerialPort:
    def __init__(self, port_name, baud_rate=19200, timeout=1):
        self.port_name = port_name
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.connection = None

    def open(self):
        self.connection = serial.Serial(self.port_name, self.baud_rate, timeout=self.timeout)

    def close(self):
        if self.connection and self.connection.is_open:
            self.connection.close()

    def write(self, data):
        if self.connection:
            self.connection.write(data)

    def read_all(self):
        if self.connection:
            return self.connection.read_all()
        return None

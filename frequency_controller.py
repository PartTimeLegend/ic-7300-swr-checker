class FrequencyController:
    def __init__(self, serial_port):
        self.serial_port = serial_port

    def set_frequency(self, frequency):
        frequency_bcd = '{:08d}'.format(int(frequency * 100))
        bcd_bytes = bytes(int(frequency_bcd[i:i+2]) for i in range(0, 8, 2))
        command = b'\xFE\xFE\x94\xE0\x05' + bcd_bytes + b'\xFD'
        self.serial_port.write(command)

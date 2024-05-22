class SWRMeasurement:
    def __init__(self, serial_port):
        self.serial_port = serial_port

    def get_swr(self):
        command = b'\xFE\xFE\x94\xE0\x14\x02\xFD'
        self.serial_port.write(command)
        response = self.serial_port.read_all()
        if len(response) >= 8:
            swr_value = response[7]
            return swr_value
        else:
            return None

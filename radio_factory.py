from serial_port import SerialPort
from frequency_controller import FrequencyController
from swr_measurement import SWRMeasurement
from csv_writer import CSVWriter

class RadioFactory:
    def __init__(self, serial_port_name, csv_filename):
        self.serial_port_name = serial_port_name
        self.csv_filename = csv_filename

    def create_serial_port(self):
        return SerialPort(self.serial_port_name)

    def create_frequency_controller(self, serial_port):
        return FrequencyController(serial_port)

    def create_swr_measurement(self, serial_port):
        return SWRMeasurement(serial_port)

    def create_csv_writer(self):
        return CSVWriter(self.csv_filename)

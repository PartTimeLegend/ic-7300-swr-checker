import csv

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_header(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Frequency (kHz)", "SWR"])

    def write_row(self, frequency, swr):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([frequency, swr])

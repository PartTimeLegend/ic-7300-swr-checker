import serial
from radio_factory import RadioFactory


def list_attached_icom_radios():
    print("Attached Icom Radios:")
    icom_radios = []
    for index, port in enumerate(serial.tools.list_ports.comports(), start=1):
        if "Icom" in port.manufacturer:
            print(f"{index}. {port.device}: {port.manufacturer} - {port.description}")
            icom_radios.append(port.device)
    return icom_radios

def select_icom_radio(icom_radios):
    if not icom_radios:
        print("No Icom radios found.")
        return None
    while True:
        selection = input("Enter the number corresponding to the Icom radio to use: ")
        try:
            index = int(selection)
            if 0 < index <= len(icom_radios):
                return icom_radios[index - 1]
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    icom_radios = list_attached_icom_radios()
    selected_radio = select_icom_radio(icom_radios)
    if selected_radio:
        print(f"Selected Icom radio: {selected_radio}")
        start_freq = float(input("Enter the start frequency in kHz: ")) * 1000
        end_freq = float(input("Enter the end frequency in kHz: ")) * 1000
        csv_file = input("Enter the CSV file name to save the results (e.g., results.csv): ")

        factory = RadioFactory(selected_radio, csv_file)
        serial_port = factory.create_serial_port()
        frequency_controller = factory.create_frequency_controller(serial_port)
        swr_measurement = factory.create_swr_measurement(serial_port)
        csv_writer = factory.create_csv_writer()

        serial_port.open()
        csv_writer.write_header()

        current_freq = start_freq
        while current_freq <= end_freq:
            frequency_controller.set_frequency(current_freq / 1000)
            swr = swr_measurement.get_swr()
            if swr is not None:
                print(f'Frequency: {current_freq / 1000} kHz, SWR: {swr}')
                csv_writer.write_row(current_freq / 1000, swr)
            else:
                print(f'Frequency: {current_freq / 1000} kHz, SWR: Error reading SWR')
                csv_writer.write_row(current_freq / 1000, "Error")
            current_freq += 1000

        serial_port.close()
    else:
        print("No Icom radio selected. Exiting...")

if __name__ == "__main__":
    main()

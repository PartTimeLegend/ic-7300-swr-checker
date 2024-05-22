# IC-7300 SWR Checker

This Python script allows you to check the SWR (Standing Wave Ratio) on an Icom IC-7300 radio and increment the VFO (Variable Frequency Oscillator) by 1 kHz within a specified frequency range. It also provides the option to save the SWR readings to a CSV file.

## Prerequisites

- Python 3.x
- pyserial library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/parttimelegend/ic-7300-swr-checker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ic-7300-swr-checker
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Connect your Icom IC-7300 radio to your computer via the appropriate serial interface.

2. Run the script:

    ```bash
    python main.py
    ```

3. Follow the on-screen prompts to enter the start and end frequencies, serial port name, and CSV file name to save the results.

4. The script will increment the frequency by 1 kHz, print the SWR at each step, and save the results to the specified CSV file.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

#!/usr/bin/env python

import serial
import time
import argparse

# Configure the serial connection
BAUD_RATE = 38400      # Adjust based on your device's baud rate
LOG_FILE = 'serial_log.txt'


"""Main function to configure GPS module."""
parser = argparse.ArgumentParser(description="Log output of Arduino.")
parser.add_argument("-p", "--port", type=str, default="/dev/ttyUSB0", help="Serial port (e.g., COM3 or /dev/ttyUSB0)", required=True)

args = parser.parse_args()

try:
    # Open serial connection
    with serial.Serial(args.port, BAUD_RATE, timeout=1) as ser, open(f"{args.port.replace("/dev/","")}_{LOG_FILE}", 'a') as log_file:
        print(f"Logging data from {args.port} at {BAUD_RATE} baud...")

        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"{timestamp} - {line}\n"
                print(log_entry, end='')  # Print to console
                log_file.write(log_entry)  # Write to file
                log_file.flush()  # Ensure data is written immediately

except serial.SerialException as e:
    print(f"Error: {e}")

except KeyboardInterrupt:
    print("\nLogging stopped by user.")

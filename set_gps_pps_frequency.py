#!/usr/bin/env python3

import serial
import time
import argparse

# PMTK command to set update rate to 5 Hz (200ms interval)
BAUD_RATE = 38400      # Adjust based on your device's baud rate
SET_UPDATE_RATE_5HZ = b"$PMTK220,200*2C\r\n"

def send_command(ser, command):
    """Sends a PMTK command to the GPS module and prints response."""
    ser.write(command)
    time.sleep(0.1)  # Small delay for processing
    response = ser.read(ser.in_waiting).decode(errors='ignore')  # Read any available response
    if response:
        print("GPS Response:", response)

def main():
    """Main function to configure GPS module."""
    parser = argparse.ArgumentParser(description="Configure Adafruit MTK3339 GPS PPS output rate to 5Hz.")
    parser.add_argument("-p", "--port", type=str, default="/dev/ttyUSB0", help="Serial port (e.g., COM3 or /dev/ttyUSB0)", required=True)
    
    args = parser.parse_args()

    try:
        with serial.Serial(args.port, BAUD_RATE, timeout=1) as ser:
            print(f"Connected to {args.port} at {BAUD_RATE} baud")

            # Send command to update rate to 5Hz
            print("Setting GPS PPS update rate to 5Hz...")
            send_command(ser, SET_UPDATE_RATE_5HZ)

            print("Configuration complete!")

    except serial.SerialException as e:
        print(f"Serial error: {e}")

if __name__ == "__main__":
    main()

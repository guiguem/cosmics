import sys
import simpleaudio as sa
import serial
from time import sleep

# pip uninstall simpleaudio
# pip install git+https://github.com/cexen/py-simple-audio.git

# 1. Load into memory ONCE before the loop
# wave_obj = sa.WaveObject.from_wave_file("click_short.wav")
wave_obj = sa.WaveObject.from_wave_file("canard_court.wav")

ser = serial.Serial('/dev/cu.usbmodem11402', 38400, timeout=1)

print("Listening to port... Press Ctrl+C to stop.")
try:
    while True:
        # Check for serial data
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            print(line)

            # 2. Play the pre-loaded object directly
            # This happens nearly instantaneously
            wave_obj.play()
            
        # 3. Reduce sleep to the absolute minimum needed for CPU stability
        # 0.001 is usually safe for high-frequency polling
        sleep(0.001) 
except KeyboardInterrupt:
    print("\nStopping...")
finally:
    ser.close()
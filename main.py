import subprocess
import time
import pyautogui
import psutil
import sys
import json

# start fn
def main():
    read_value()

# read config.json data
def read_value():
    with open('./config.json', 'r') as f:
        config = json.load(f)
    
    files = config["files"]
    
    for file in files:
        exe = file["exe"]
        path = file["path"]
        clicks = file["clicks"]
        print(f"exe: {exe}, path: {path}")
        
        process = subprocess.Popen([path], shell=True)
        
        # try to wait for second open exe.
        # reason is idw why steam open original exe file will close first exe then open again.
        # to avoid this strange condition so i wait a second to read the actual pid.
        if "exe" in path:
            time.sleep(10)
        
        found_pid = find_file(exe)
        time.sleep(3)  # try to wait for passing unity loading logo.
        click_process(exe,clicks)
        time.sleep(3)  # try to wait for the drop items appear.
        terminate_process(found_pid)
        time.sleep(3)  # not necessary, just my cmd vision demand.
        print("end")

# get the target pid, will try 5 times in every second
def find_file(exe):
    def find_process_by_exe_name(exe_name):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'].lower() == exe_name.lower():
                return proc.info['pid']
        return None

    max_attempts = 5
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        found_pid = find_process_by_exe_name(exe+".exe")
        
        if found_pid is not None:
            print(found_pid)
            return found_pid
            break
        else:
            print(f"Attempt failed in {attempts}.")
            if attempts == max_attempts:
                print(f"Till {max_attempts} attempts but still couldn't find {exe}. Closing the process.")
                time.sleep(3)
                sys.exit()
        time.sleep(1)

# click works
def click_process(exe,clicks):
    # click target file window middle transform
    app_window = pyautogui.getWindowsWithTitle(exe)[0]
    center_x = app_window.left + app_window.width // 2
    center_y = app_window.top + app_window.height // 2
    max_click_time = clicks
    now_click_time = 0
    while now_click_time < max_click_time:
        now_click_time += 1
        pyautogui.click(center_x, center_y)

# work done, close target file
def terminate_process(pid):
    try:
        subprocess.run(['taskkill', '/F', '/PID', str(pid)], check=True)
        print(f"success end process {pid}")
    except subprocess.CalledProcessError as e:
        print(f"fail end process {pid}: {e}")
        terminate_process(pid)

# start process
if __name__ == "__main__":
    main()
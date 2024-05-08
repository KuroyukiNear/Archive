# Kuroyuki Near
# 03 April 2024

import os
import time
import threading

stil_loading = True

def loading():
    while stil_loading:
        os.system("cls")
        print("Loading...  _")
        time.sleep(0.5)
        os.system("cls")
        print("Loading...  \\")
        time.sleep(0.5)
        os.system("cls")
        print("Loading...  |")
        time.sleep(0.5)
        os.system("cls")
        print("Loading...  /")
        time.sleep(0.5)
    os.system("cls")
    print("Loading complete.")

def main():
    global stil_loading

    # Start doing your stuff
    loading_thread = threading.Thread(target=loading)
    loading_thread.start()

    time.sleep(5) # Do your stuff

    # Your stuff is done
    stil_loading = False
    loading_thread.join()

if __name__ == "__main__":
    main()
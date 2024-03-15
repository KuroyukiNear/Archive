# Kuroyuki Near
# 15 March 2024

import os
import time
import random
import colorama
from colorama import *

colorama.init(autoreset=True)

full = "█"
empty = "_"

current_value = 0

def draw_bar(text_above, colour, complete_text) -> None:
    global current_value
    color_attribute = getattr(Fore, colour)

    if current_value < 100:
        current_value += 1
        os.system("cls")

        remaining_bars = round(current_value / 100 * 20)
        lost_bars = 20 - remaining_bars

        print(f"{color_attribute}{text_above}\n|{color_attribute}{remaining_bars * full}{lost_bars * empty}{Fore.RESET}| {current_value}%")
        if current_value == 100:
            print(f"{color_attribute}\n{complete_text}")
    else:
        pass

def bar(text_above, colour, complete_text):
    while True:
        draw_bar(text_above, colour, complete_text)
        if current_value == 100:
            break
        sleeptime = random.randint(1, 5)
        sleeptime = sleeptime / 10
        time.sleep(sleeptime) # 0.1 to 0.5 seconds
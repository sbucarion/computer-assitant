import sys

input_detector_path = r"C:\Users\sbucarion1\Documents\code\pierre\autokm"
coordinates_path = r"C:\Users\sbucarion1\Documents\code\pierre\autokm"

sys.path.insert(0, input_detector_path)
sys.path.insert(0, coordinates_path)

from input_listener import input_detector
from process_image import get_coordinates

import os
import pyautogui
from pytesseract import pytesseract
from numba import njit
from thefuzz import fuzz
from datetime import datetime
import wmi
from PIL import ImageGrab
import mss
import cv2
import numpy as np


def get_screenshot_dir():
    current_dir = os.getcwd()
    
    #When getting current dir it gives dir of calling file and not where this file is
    screenshot_dir = current_dir + "\\autokm\\screenshot_folder"
    
    if not screenshot_dir:
        os.mkdir(screenshot_dir)
        
    else:
        return screenshot_dir
    
    
def screenshot_screen(screenshot_dir):
    with mss.mss() as sct:

        # Get count of monitors
        monitor_count = len(sct.monitors)
        
        for i in range(1, monitor_count):
            monitor_number = i
            mon = sct.monitors[monitor_number]

            # The screen part to capture
            monitor = {
                "top": mon["top"],
                "left": mon["left"],
                "width": mon["width"],
                "height": mon["height"],
                "mon": monitor_number,
            }
            output = screenshot_dir + (r"\monitor{}.png".format(str(i)))

            # Grab the data
            sct_img = sct.grab(monitor)

            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


def click_on_command(command):
    command = command.lower()
    
    screenshot_dir = get_screenshot_dir()
    screenshot_screen(screenshot_dir)
    
    results = get_coordinates(command, screenshot_dir)
    
    if results is not None:
        return results
        #pyautogui.click(coors)

    else:
        return "not found"
    
    
def command_handler(command):
    if 'pause' in command:
        pyautogui.click(900,500)
        #pyautogui.press('space')
        
    if 'enter' in command:
        pyautogui.press('enter')    
        
    if 'space' in command:
        pyautogui.press('space')
        
#     else:
#         click_on_command(command)


def command_listener(activator="pierre"):
    command = input_detector(activator)
    return command


if __name__ == "__main__":
    click_on_command(command)
    command_listener()
    get_screenshot_dir()
import struct
import ctypes
import time
import os
import random


SPI_SETDESKWALLPAPER = 20


def is_64_windows():
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper(WALLPAPER_PATH):
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH , 3)
    if not r:
        print(ctypes.WinError())


while True:
    wlp = os.listdir("Duvar Kağıtları/")
    wallpaper = random.choice(wlp)
    path = fr'C:\Users\umuts\Desktop\Rastgele Wallpaper\Duvar Kağıtları\{wallpaper}'
    change_wallpaper(path)
    time.sleep(2)
import win32gui
import win32api
import win32con
import time
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import pygame
 
def invert_colors():
    desktop_window_id = 0
    desktop_dc = win32gui.GetDC(desktop_window_id)
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    win32gui.StretchBlt(desktop_dc, 0, 0, screen_width, screen_height, desktop_dc, 0, 0, screen_width, screen_height, win32con.NOTSRCCOPY)
    win32gui.BitBlt(desktop_dc, 0, 0, screen_width, screen_height, desktop_dc, 0, 0, win32con.NOTSRCCOPY)
    win32gui.ReleaseDC(desktop_window_id, desktop_dc)

def restore_colors():
    desktop_window_id = 0
    desktop_dc = win32gui.GetDC(desktop_window_id)
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    win32gui.BitBlt(desktop_dc, 0, 0, screen_width, screen_height, desktop_dc, 0, 0, win32con.SRCCOPY)
    win32gui.ReleaseDC(desktop_window_id, desktop_dc)

for i in range(6):
    invert_colors()
    time.sleep(0.3)
    restore_colors()
    time.sleep(0.3)

time.sleep(2.5)  # Sleep for 2.5 sec

desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
sw = GetSystemMetrics(0)
sh = GetSystemMetrics(1)
a = GetSystemMetrics(SM_CXSCREEN)
b = GetSystemMetrics(SM_CYSCREEN)
 
start_time = time.time()
while time.time() - start_time < 6:
    brush = CreateSolidBrush(RGB(
        0,
        255,
        0,
    ))
    PatBlt(desk, 0, 0, x, y, PATINVERT)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    BitBlt(desk, 10, 10, w, h, desk, 12, 12, SRCAND)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
 
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCINVERT)
    DeleteObject(brush)
    time.sleep(0)

time.sleep(2)

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((0, 0, 0))
pygame.mouse.set_visible(False)
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()

# by OverlordV1per github page https://github.com/OverlordV1per

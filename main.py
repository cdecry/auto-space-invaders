from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll
import pyautogui
from PIL import Image
import time
import os
from pathlib import Path

def get_window_info(window_title):
    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)
    for window in windows:
        if window_title in window.get("kCGWindowName", ""):
            window_id = window["kCGWindowNumber"]
            window_rect = window["kCGWindowBounds"]
            x, y, w, h = window_rect["X"], window_rect["Y"], window_rect["Width"], window_rect["Height"]
            return x, y, w, h
    return None

def capture_game_window(x, y, w, h):
    game_window_pos = (x, y)
    game_window_size = (w, h)

    screenshot = pyautogui.screenshot(region=(int(game_window_pos[0]), int(game_window_pos[1]), int(game_window_size[0]), int(game_window_size[1])))
    return screenshot

def is_specific_screen_displayed():
    pyautogui.useImageNotFoundException()
    exit_button_pos = None
    try:
        exit_button_pos = pyautogui.locateOnScreen('exit_button.png', confidence=0.6)
        print('image found')
    except pyautogui.ImageNotFoundException:
        pass

    if exit_button_pos:
        return True
    else:
        return False

def main():
    window_title = "Starimu"
    window_info = get_window_info(window_title)
    if not window_info:
        print("Window not found")
        return
    
    x, y, w, h = window_info
    print(f"Window Found. Coordinates: x={x}, y={y}, width={w}, height={h}")

    while True:
        game_screenshot = capture_game_window(x, y, w, h)

        if is_specific_screen_displayed():
            print("Game ended")
            break

if __name__ == "__main__":
    main()
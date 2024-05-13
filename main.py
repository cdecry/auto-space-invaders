from Quartz.CoreGraphics import CGEventCreateMouseEvent, kCGEventMouseMoved, kCGEventLeftMouseDown, kCGEventLeftMouseUp, CGEventPost, kCGEventSourceStateHIDSystemState
import Quartz
import pyautogui
from PIL import Image
import time
import keyboard
from pathlib import Path

def detect_image(img, confidence):
    pyautogui.useImageNotFoundException()
    detected = None
    try:
        detected = pyautogui.locateOnScreen(img, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        pass

    return detected

def mouse_click(x, y):
    move_event = CGEventCreateMouseEvent(None, kCGEventMouseMoved, (x, y), 0)
    CGEventPost(kCGEventSourceStateHIDSystemState, move_event)
    event = Quartz.CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (x, y), 0)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)

    time.sleep(0.1)

    event = Quartz.CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, (x, y), 0)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)


def main():

    while True:
        pyautogui.keyDown('space')
        if keyboard.is_pressed(1):
            break
            # pyautogui.keyUp('space')
        spaceship_pos = detect_image('spaceship.png', 0.8)
        laser_pos = detect_image('laser.png', 0.97)

        if spaceship_pos:
            # if laser_pos and laser_pos[0] >= spaceship_pos[0] and laser_pos[1] <= spaceship_pos[0] + spaceship_pos[2]:
            #     pyautogui.keyDown('left')
            #     time.sleep(0.2)
            #     pyautogui.keyUp('left')

            alien_pos = detect_image('alien1.png', 0.7)
            if alien_pos:
                if spaceship_pos[0] - alien_pos[0] > 10:
                    pyautogui.keyDown('left')
                    time.sleep(0.5)
                    pyautogui.keyUp('left')
                elif spaceship_pos[0] - alien_pos[0] < 10:
                    pyautogui.keyDown('right')
                    time.sleep(1)
                    pyautogui.keyUp('right')

        if detect_image('exit_button.png', 0.7):
            mouse_click(715, 552)
            time.sleep(4)
            mouse_click(1183, 196)
            time.sleep(0.5)

            mouse_click(1002, 447)
            time.sleep(0.5)

            time.sleep(1)
            mouse_click(718, 572)
            time.sleep(1)
            mouse_click(650, 511)
            time.sleep(3)

            mouse_click(718, 501)
            time.sleep(1)
            mouse_click(788, 433)
            time.sleep(1)
            mouse_click(715, 601)
            time.sleep(3)

if __name__ == "__main__":
    main()
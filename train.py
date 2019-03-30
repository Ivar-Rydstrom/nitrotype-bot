import numpy as np
from PIL import ImageGrab
from PIL import ImageOps
import cv2
import pytesseract
import pyautogui
from pynput.keyboard import Key, Listener
from Convert import convert_to_char

pytesseract.pytesseract.tesseract_cmd = r'E:\Ivar\Apps\Tesseract\tesseract.exe'


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # processed_img = cv2.Canny(processed_img, threshold1=700, threshold2=100)
    return processed_img


def saveKey(key):
    np.save('traindata/' + key + '.npy', grab_image())
    print("saved: " + key)


def grab_image():
    raw = ImageGrab.grab(bbox=(1920 / 3 + 60, 2.05 * 1080 / 3, 2 * 1920 / 3 - 70, 1.58 * 1080 / 2))
    w, h = raw.size
    raw = ImageOps.crop(raw, (9, 31, 475, 40))
    raw = raw.resize((200, 300))
    screen = np.array(raw)
    new_screen = process_img(screen)
    cv2.imshow('window', new_screen)
    # cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    return new_screen


def on_press(key):
    global lastKey_shift
    if key == Key.esc:
        return False
    elif key == Key.shift_l or key == Key.shift_r:
        lastKey_shift = True
    elif lastKey_shift:
        key = "shift_" + key.char
        lastKey_shift = False
        saveKey(key)
    elif key == Key.space:
        key = " "
        lastKey_shift = False
        saveKey(key)
    else:
        lastKey_shift = False
        saveKey(key.char)



if __name__ == "__main__":
    with Listener(on_press=on_press) as listener:
        lastKey_shift = False
        listener.join()

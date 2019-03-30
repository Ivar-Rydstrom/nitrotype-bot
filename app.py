import numpy as np
from PIL import ImageGrab
from PIL import ImageOps
import cv2
import pytesseract
import pyautogui
from Img import Img

pytesseract.pytesseract.tesseract_cmd = r'E:\Ivar\Apps\Tesseract\tesseract.exe'


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # processed_img = cv2.Canny(processed_img, threshold1=700, threshold2=100)
    return processed_img


def get_char(img):
    text = pytesseract.image_to_string(img, config='--psm 10')
    return text


def type_char(char):
    pyautogui.keyDown(char)
    pyautogui.keyUp(char)


def type_char_shift(char):
    pyautogui.keyDown('shift')
    pyautogui.keyDown(char)
    pyautogui.keyUp(char)
    pyautogui.keyUp('shift')


while(True):
    img = Img()
    # new_screen = screen
    detection = get_char(img.get_screen())
    if detection:
        char = detection[0]
        if char.startswith('shift_'):
            type_char_shift(char)
        else:
            type_char(char)

        print(char)
    img.show()
    # cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
